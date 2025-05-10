import os
from pydub import AudioSegment
import speech_recognition as sr

# Update these paths as needed
FFMPEG_PATH = r"C:\Users\SKJHA\ffmpeg\bin\ffmpeg.exe"
FFPROBE_PATH = r"C:\Users\SKJHA\ffmpeg\bin\ffprobe.exe"

def transcribe_audio(mp3_input_path, wav_output_path):
    # Configure pydub to find FFmpeg
    AudioSegment.converter = FFMPEG_PATH
    AudioSegment.ffprobe = FFPROBE_PATH

    if not os.path.exists(mp3_input_path):
        print("MP3 file not found.")
        return

    # Convert to WAV
    audio = AudioSegment.from_mp3(mp3_input_path)
    audio.export(wav_output_path, format="wav")

    # Recognize speech
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_output_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        # Remove the emoji and just print text
        print("Transcription:\n", text)
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
