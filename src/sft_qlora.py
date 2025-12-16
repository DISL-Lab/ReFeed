# Copyright 2025 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Supervised fine-tuning script for decoder language models.

Usage:
    accelerate launch --config_file=configs/zero3.yaml src/open_r1/sft.py \
        --model_name_or_path Qwen/Qwen2.5-1.5B-Instruct \
        --dataset_name HuggingFaceH4/Bespoke-Stratos-17k \
        --learning_rate 2.0e-5 \
        --num_train_epochs 1 \
        --packing \
        --max_seq_length 4096 \
        --per_device_train_batch_size 4 \
        --gradient_accumulation_steps 4 \
        --gradient_checkpointing \
        --bf16 \
        --logging_steps 5 \
        --eval_strategy steps \
        --eval_steps 100 \
        --output_dir data/Qwen2.5-1.5B-Open-R1-Distill
"""

from accelerate import Accelerator
from datasets import load_dataset
from deepspeed.accelerator import get_accelerator
from transformers import AutoTokenizer
from trl import (
    ModelConfig,
    ScriptArguments,
    SFTConfig,
    SFTTrainer,
    TrlParser,
    get_peft_config,
    get_quantization_config,
)

# Initialize accelerator and clear cache
get_accelerator().empty_cache()
accelerator = Accelerator()


def setup_tokenizer(model_args):
    """Initialize and configure tokenizer."""
    tokenizer = AutoTokenizer.from_pretrained(
        model_args.model_name_or_path,
        trust_remote_code=model_args.trust_remote_code,
        use_fast=True,
    )
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"
    return tokenizer


def get_model_kwargs(model_args, training_args):
    """Prepare model initialization arguments."""
    quantization_config = get_quantization_config(model_args)
    use_cache = not training_args.gradient_checkpointing
    
    return dict(
        revision=model_args.model_revision,
        trust_remote_code=model_args.trust_remote_code,
        attn_implementation=model_args.attn_implementation,
        torch_dtype=model_args.torch_dtype,
        use_cache=use_cache,
        quantization_config=quantization_config,
    )


def load_training_dataset(script_args):
    """Load dataset from specified path."""
    return load_dataset(script_args.dataset_name)


def main(script_args, training_args, model_args):
    """Main training function."""
    # Setup model and tokenizer
    model_kwargs = get_model_kwargs(model_args, training_args)
    training_args.model_init_kwargs = model_kwargs
    tokenizer = setup_tokenizer(model_args)
    
    # Load dataset
    dataset = load_training_dataset(script_args)
    
    # Prepare evaluation dataset
    eval_dataset = None
    if training_args.eval_strategy != "no":
        eval_dataset = dataset[script_args.dataset_test_split]
    
    # Initialize trainer
    trainer = SFTTrainer(
        model=model_args.model_name_or_path,
        args=training_args,
        train_dataset=dataset[script_args.dataset_train_split],
        eval_dataset=eval_dataset,
        processing_class=tokenizer,
        peft_config=get_peft_config(model_args),
    )
    
    # Train model
    trainer.train()
    
    # Save model
    trainer.save_model(training_args.output_dir)
    
    # Push to hub if requested
    if training_args.push_to_hub:
        trainer.push_to_hub(dataset_name=script_args.dataset_name)


if __name__ == "__main__":
    parser = TrlParser((ScriptArguments, SFTConfig, ModelConfig))
    script_args, training_args, model_args = parser.parse_args_and_config()
    main(script_args, training_args, model_args)