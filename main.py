import torch
from transformers import pipeline
import whisper
import os

# Load Whisper model (base or small to keep memory usage lower if needed)
whisper_model = whisper.load_model("base")

# Load BART summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def transcribe_audio(video_path):
    print("Transcribing audio...")
    result = whisper_model.transcribe(video_path)
    return result["text"]

def summarize_text(text):
    print("Summarizing transcription...")
    # Huggingface's summarizer has a max token limit (~1024 tokens),
    # so we might need to chunk text if it's too long.
    if len(text) > 3000:
        text = text[:3000]  # simple truncation for now

    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def process_video(video_path):
    transcription = transcribe_audio(video_path)
    summary = summarize_text(transcription)
    return transcription, summary
