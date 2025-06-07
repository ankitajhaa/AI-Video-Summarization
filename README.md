# 🎥 AI Video Summarization & Quiz Generation

This project is an end-to-end AI application that takes a video as input, transcribes the audio using OpenAI's Whisper, summarizes the content using BART (from Huggingface), and generates quiz questions based on the summarized content. It also features a Flask-based web interface for easy interaction.

---

## 🚀 Features

- 🎬 Upload a video file (MP4)
- 🎙️ Extract and transcribe audio using Whisper
- 🧠 Summarize the transcribed text using BART
- ❓ Automatically generate quiz questions from the summary
- 🌐 Simple and clean Flask web interface

---

## 🛠️ Tech Stack

| Component         | Technology             |
|------------------|------------------------|
| Audio Extraction | `moviepy`, `pydub`     |
| Transcription     | `openai-whisper`       |
| Summarization     | `transformers` (BART)  |
| Quiz Generation   | Custom NLP / QG Model  |
| Web Interface     | `Flask`, `HTML`, `CSS` |

---

## 📁 Folder Structure

video-summarizer-quiz/
│
├── main.py
├── extract_audio.py
├── transcribe_audio.py
├── summarize_transcription.py
├── generate_quiz.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
