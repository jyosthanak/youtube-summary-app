import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import os
import urllib.parse

# ✅ THIS MUST BE FIRST Streamlit command
st.set_page_config(page_title="YouTube Summary Generator", layout="centered")

# Everything else comes after
def extract_video_id(url):
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)
    return query_params.get("v", [None])[0]

def get_transcript(video_url):
    try:
        video_id = extract_video_id(video_url)
        if not video_id:
            raise ValueError("Invalid YouTube URL")
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        if not transcript:
             raise ValueError("No transcript found for this video")
        full_text = " ".join([item['text'] for item in transcript])
        return full_text
    except Exception as e:
        st.error(f"Transcript fetch error: {str(e)}")
        return None

# Cache HuggingFace summarizer model
@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()

def summarize_text(text):
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summary = ""
    for chunk in chunks:
        result = summarizer(chunk, max_length=150, min_length=40, do_sample=False)
        summary += result[0]['summary_text'] + "\n\n"
    return summary.strip()

# --- UI ---
st.title("🎥 YouTube Summary Generator")

video_url = st.text_input("Enter YouTube video URL")

if video_url:
    with st.spinner("Fetching transcript and summarizing..."):
        transcript = get_transcript(video_url)
        if transcript:
            summary = summarize_text(transcript)
            st.success("Summary:")
            st.markdown(summary)
            st.download_button("📄 Download Summary", summary, file_name="summary.txt")
        else:
            st.error("Failed to fetch transcript. Try a different video.")
