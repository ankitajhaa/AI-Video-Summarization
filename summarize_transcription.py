# summarize_transcription.py

from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    # Handle long texts by chunking
    max_chunk_length = 1024
    if len(text) > max_chunk_length:
        chunks = [text[i:i+max_chunk_length] for i in range(0, len(text), max_chunk_length)]
    else:
        chunks = [text]

    summary = ""
    for chunk in chunks:
        result = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summary += result[0]['summary_text'] + " "
    return summary.strip()

# Example usage:
if __name__ == "__main__":
    with open("transcription.txt", "r") as file:
        transcription = file.read()
    
    summary = summarize_text(transcription)
    print("\n📝 Summary:\n", summary)
