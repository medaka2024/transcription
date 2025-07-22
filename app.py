import streamlit as st
import tempfile
import os
from openai import OpenAI

st.set_page_config(page_title="Whisperで音声文字起こし", layout="centered")
st.title("🎙️ Whisper 音声文字起こし")
st.markdown("MP3/WAVファイルをアップロードすると、OpenAI Whisper API で文字起こしします。")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

uploaded_file = st.file_uploader("音声ファイルをアップロード", type=["mp3", "wav", "m4a"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    with open(tmp_file_path, "rb") as audio_file:
        with st.spinner("文字起こし中..."):
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
            )
        st.success("完了！")
        st.markdown("### 文字起こし結果")
        st.write(transcript.text)
