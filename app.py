import streamlit as st
import whisper
import tempfile

st.title("🎙️ Whisper ローカル文字起こし")
st.markdown("アップロードした音声をローカルのWhisperで文字起こしします。")

uploaded_file = st.file_uploader("音声ファイルを選択してください", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    st.info("文字起こし中... しばらくお待ちください。")
    model = whisper.load_model("small")  # small, base, tiny などサイズ調整可能
    result = model.transcribe(tmp_path, language="ja")

    st.subheader("文字起こし結果")
    st.write(result["text"])
