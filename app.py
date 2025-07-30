import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import urllib.parse

st.set_page_config(page_title="YouTube Summary Generator", layout="centered")
st.title("🎥 YouTube Summary Generator")

# 📦 Load summarization model
@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()

# 🔍 Extract video ID
def extract_video_id(url):
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)
    return query_params.get("v", [None])[0]

# 🧠 Summary generator
def summarize_text(text):
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summary = ""
    for chunk in chunks:
        result = summarizer(chunk, max_length=150, min_length=40, do_sample=False)
        summary += result[0]['summary_text'] + "\n\n"
    return summary.strip()

# 🎬 Transcript fetcher
def get_transcript(video_url):
    try:
        video_id = extract_video_id(video_url)
        if not video_id:
            raise ValueError("Invalid YouTube URL")
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        if not transcript:
            raise ValueError("No transcript found")
        return " ".join([item['text'] for item in transcript])
    except Exception as e:
        st.error(f"Transcript fetch error: {str(e)}")
        return None

# 🖥️ UI
video_url = st.text_input("Enter YouTube video URL")

if video_url:
    with st.spinner("Fetching transcript and summarizing..."):
        transcript = get_transcript(video_url)
        if transcript:
            summary = summarize_text(transcript)
            st.success("Summary:")
            st.markdown(summary)
            st.download_button("📄 Download Summary", summary, file_name="summary.txt")

# ✍️ Fallback input method
st.markdown("---")
st.subheader("📋 Or paste your own transcript below")

manual_text = st.text_area("Paste transcript here (if YouTube fetch fails)", height=200)

if manual_text:
    with st.spinner("Summarizing..."):
        summary = summarize_text(manual_text)
        st.success("Summary:")
        st.markdown(summary)
        st.download_button("📄 Download Summary", summary, file_name="summary.txt")
