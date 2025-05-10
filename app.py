import streamlit as st
from main import process_video  # assuming your main logic is in main.py

st.set_page_config(page_title="Video Summarizer", layout="centered")

st.title("Video Summarization App")
st.write("Upload a video file to transcribe and summarize its content.")

# Upload video
uploaded_file = st.file_uploader("Choose a video...", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    with open("temp_video.mp4", "wb") as f:
        f.write(uploaded_file.read())
    
    st.info("Processing video... This might take a while.")
    transcription, summary = process_video("temp_video.mp4")

    st.subheader("Summary:")
    st.text_area("Full Text:", transcription, height=200)

