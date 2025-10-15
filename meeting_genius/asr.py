import os
import math
import difflib

import torch
import torchaudio
from pydub import AudioSegment
from transformers import WhisperProcessor, WhisperForConditionalGeneration


def get_config():
    return  {
        "model_name": "openai/whisper-medium",
        "device": "cuda" if torch.cuda.is_available() else "cpu",
        "base_path": os.getcwd(),
        "file_name": "your file name",
        "file_format": "your file fromat",
        "export_file_name": "your export file name",
        "export_file_format": "your export file name fromat",
        "chunk_seconds": 20,
        "overlap_seconds": 5,
    }


def convert_audio(config, file_path):
    AudioSegment.converter = os.path.join(config["base_path"], "ffmpeg.exe")
    AudioSegment.ffprobe = os.path.join(config["base_path"], "ffprobe.exe")
    audio = AudioSegment.from_file(
        file_path,
        format=config["file_format"]
    )
    audio = audio.set_channels(1).set_frame_rate(16000)
    audio.export(
        os.path.join(config["base_path"], config["export_file_name"]),
        format=config["export_file_format"]
    )


def load_model(config):
    processor = WhisperProcessor.from_pretrained(config["model_name"])
    model = WhisperForConditionalGeneration.from_pretrained(config["model_name"])
    model.to(config["device"])
    model.config.forced_decoder_ids = None
    return processor, model


def transcribe_audio(config, processor, model):
    audio_input, sr = torchaudio.load(config["export_file_name"])

    if sr != 16000:
        resampler = torchaudio.transforms.Resample(sr, 16000)
        audio_input = resampler(audio_input)

    chunk_size = config["chunk_seconds"] * 16000
    overlap_size = config["overlap_seconds"] * 16000
    num_chunks = math.ceil(audio_input.shape[1] / (chunk_size - overlap_size))

    chunks = []
    for i in range(num_chunks):
        start = i * (chunk_size - overlap_size)
        end = min(start + chunk_size, audio_input.shape[1])
        chunk = audio_input[:, start:end].squeeze()
        inputs = processor(chunk, sampling_rate=16000, return_tensors="pt").input_features
        inputs = inputs.to(config["device"])
        generated_ids = model.generate(inputs, max_length=1000)
        text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        chunks.append(text)
    return chunks


def merge_transcriptions(chunks, min_overlap_chars=15, inspect_chars=120):
    if not chunks:
        return ""

    transcriptions = chunks[0]
    for text in chunks[1:]:
        if not text:
            continue

        a = transcriptions[-inspect_chars:] if len(transcriptions) > 0 else ""
        b = text[:inspect_chars] if len(text) > 0 else ""
        match = difflib.SequenceMatcher(None, a, b).find_longest_match(0, len(a), 0, len(b))

        if match.size >= min_overlap_chars:
            text = text[match.size:]

        transcriptions += text
    return transcriptions


def main(file_path):
    config = get_config()
    convert_audio(config, file_path)
    processor, model = load_model(config)
    chunks = transcribe_audio(config, processor, model)
    transcriptions = merge_transcriptions(chunks)
    return transcriptions


if __name__ == "__main__":
    file_path = "your file path"
    transcriptions = main(file_path)