import streamlit as st
import openai
import tempfile

st.set_page_config(page_title="Whisperで音声文字起こし", layout="centered")

st.title("🎙️ Whisper 音声文字起こし")
st.markdown("MP3/WAVファイルをアップロードすると、OpenAI Whisper API で文字起こしします。")

# OpenAI APIキーの入力（セキュリティ重視なら secrets に分ける）
openai.api_key = st.secrets["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"]

uploaded_file = st.file_uploader("音声ファイルをアップロード", type=["mp3", "wav", "m4a"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    with open(tmp_file_path, "rb") as audio_file:
        with st.spinner("文字起こし中..."):
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
        st.success("完了！")
        st.markdown("### 文字起こし結果")
        st.write(transcript["text"])
