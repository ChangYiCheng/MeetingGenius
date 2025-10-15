import torch
from transformers import pipeline
from huggingface_hub import login


def get_config():
    return {
        "token" :"your hugging face token",
        "model_name": "meta-llama/Llama-3.2-3B-Instruct",
        "device_map": 0 if torch.cuda.is_available() else -1,
        "max_new_tokens": 3000,
    }


def load_model(config):
    login(token=config["token"])
    pipe = pipeline(
        "text-generation",
        model=config["model_name"],
        torch_dtype=torch.bfloat16,
        device_map=config["device_map"],
    )
    return pipe


def build_prompt(transcriptions):
    prompt = f"your prompt {transcriptions}"

    messages = [
        {"role": "system", "content": "your content"},
        {"role": "user", "content": prompt},
    ]
    return messages


def generate_summary(config, pipe, messages):
    outputs = pipe(
        messages,
        max_new_tokens=config["max_new_tokens"],
    )
    summary = outputs[0]["generated_text"][-1]['content']
    return summary


def text_translation(config, pipe, summary, language):
    prompt = f'''yuor prompt {language} {summary}'''
    messages1 = [
        {"role": "system", "content": "your content"},
        {"role": "user", "content": prompt},
    ]
    outputs = pipe(
        messages1,
        max_new_tokens=config["max_new_tokens"],
    )
    summary = outputs[0]["generated_text"][-1]['content']
    return summary


def save_summary(transcriptions, summary):
    with open('work_summary.txt', 'w', encoding='utf-8') as f:
        f.write("===== 原始語音轉錄 =====\n\n")
        f.write(transcriptions)
        f.write("\n\n===== AI 生成的摘要與靈感 =====\n\n")
        f.write(summary)


def main(transcriptions, language):
    config = get_config()
    pipe = load_model(config)
    messages = build_prompt(transcriptions)
    summary = generate_summary(config, pipe, messages)
    summary = text_translation(config, pipe, summary, language)
    save_summary(transcriptions, summary)
    print("FINISH")
    return summary


if __name__ == "__main__":
    transcriptions = "system-transcribed text"
    language = "your selected language"
    summary = main(transcriptions, language)