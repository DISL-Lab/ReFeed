accelerate launch --main_process_port 33333 --config_file=/configs/zero3.yaml /src/sft_qlora.py \
    --model_name_or_path meta-llama/Llama-3.1-8B-Instruct \
    --dataset_name DISLab/SumFeed-CoT \
    --output_dir model/ReFeed-8B \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --bf16 \
    --gradient_checkpointing \
    --num_train_epochs 3 \
    --learning_rate 1e-4 \
    --logging_steps 5 \
    --packing \
    --max_seq_length 10000 \
    --use_peft \
    --lora_alpha 32 \
    --lora_r 16 \
    --warmup_ratio 0.03 \
    --lr_scheduler_type="cosine" \
    --gradient_accumulation_steps 8 \
   
