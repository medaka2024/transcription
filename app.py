import streamlit as st
import openai
import io

st.set_page_config(page_title="Whisperで音声文字起こし", layout="centered")

st.title("🎙️ Whisper 音声文字起こし")
st.markdown("MP3/WAVファイルをアップロードすると、OpenAI Whisper API で文字起こしします。")

# OpenAI APIキー（Streamlit Cloud に設定済みとする）
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

uploaded_file = st.file_uploader("音声ファイルをアップロード", type=["mp3", "wav", "m4a"])

if uploaded_file:
    audio_bytes = uploaded_file.read()
    audio_file = io.BytesIO(audio_bytes)
    audio_file.name = uploaded_file.name  # 必須：拡張子付きファイル名が必要

    with st.spinner("文字起こし中..."):
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language="ja"
        )
    
    st.success("完了！")
    st.markdown("### 文字起こし結果")
    st.write(transcript.text)
