import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from feedback_mapping import create_feedback_report

# Model Setup
model_id = "meta-llama/Llama-3.1-8B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

# Example Data
d = {
    "document": "your document here",
    "sentences": ["summary sentence 1", "summary sentence 2", "summary sentence 3"],
    "faithfulness_feedback": [1, 0, 1],  # 0 is a non-factual sentence
    "keyfacts": ["keyfact 1", "keyfact 2"],
    "completeness_feedback": [1, 0],     # 0 is a missing keyfact
    "conciseness_feedback": [1, 1, 1]    # 0 is a summary sentence which contains no keyfact
}

# Inference
doc_ = d["document"]
whole_summary = " ".join(d["sentences"])

# Generate feedback report using the module
report_text = create_feedback_report(
    sentences=d["sentences"],
    faithfulness_labels=d["faithfulness_feedback"],
    keyfacts=d["keyfacts"],
    completeness_labels=d["completeness_feedback"],
    conciseness_labels=d["conciseness_feedback"]
)

system_prompt = "Your role as an assistant involves thoroughly exploring questions through a systematic long thinking process before providing the final precise and accurate solutions. This requires engaging in a comprehensive cycle of analysis, summarizing, exploration, reassessment, reflection, backtracing, and iteration to develop well-considered thinking process. Please structure your response into two main sections: Think and Answer. In the Think section, detail your reasoning process using the specified format: <think> {thought with steps separated with '\\n\\n'} </think> Each step should include detailed considerations such as analisying questions, summarizing relevant findings, brainstorming new ideas, verifying the accuracy of the current steps, refining any errors, and revisiting previous steps. In the Answer section, based on various attempts, explorations, and reflections from the Think section, systematically present the final solution that you deem correct. The solution should remain a logical, accurate, concise expression style and detail necessary step needed to reach the conclusion, formatted as follows: <answer> {final formatted, precise, and clear solution} </answer> Now, try to solve the following question through the above guidelines:"

user_prompt = f"""
Your goal is to deliberate on the provided feedback and propose actionable and specific aggregated feedback based on it.

Instructions:
1. Deliberate on the characteristics an ideal summary should achieve.
2. Assess and choose the validity of the given feedback in improving the summary considering feedback quality criteria:
- Faithfulness: Out-of-article, Entity, Relation, Sentence errors
- Completeness: missing key content
- Conciseness: unnecessary or non-key content
3. Aggregate the valid feedback and revise the summary by incorporating it.
4. Check whether revisions harm other quality dimensions.

Document:
{doc_}

Summary:
{whole_summary}

Feedback:
{report_text}
"""

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt},
]

input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

terminators = [
    tokenizer.eos_token_id,
    tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

outputs = model.generate(
    input_ids,
    max_new_tokens=7000,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6
)

gen = outputs[0][input_ids.shape[-1]:]
response = tokenizer.decode(gen, skip_special_tokens=True)