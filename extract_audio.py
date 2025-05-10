from moviepy import VideoFileClip
import logging

# Suppress unnecessary MoviePy logs
logging.getLogger("moviepy").setLevel(logging.ERROR)

def extract_audio_from_video(video_path, mp3_output_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(mp3_output_path)
    video.close()
