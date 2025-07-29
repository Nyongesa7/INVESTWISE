# ---------------------- voice_input.py ----------------------

import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode
import whisper
import av
import ffmpeg

model = whisper.load_model("base")

class AudioProcessor:
    def __init__(self):
        self.transcription = ""

    def recv(self, frame: av.AudioFrame) -> av.AudioFrame:
        audio = frame.to_ndarray().flatten().astype("float32") / 32768.0
        result = model.transcribe(audio)
        self.transcription = result['text']
        return frame

def voice_input_box():
    ctx = webrtc_streamer(
        key="speech",
        mode=WebRtcMode.SENDRECV,
        audio_receiver_size=1024,
        audio_processor_factory=AudioProcessor,
        media_stream_constraints={"audio": True, "video": False},
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    )
    if ctx.state.playing:
        st.write("🎙️ Listening... Speak now")
    if hasattr(ctx.audio_processor, 'transcription'):
        return ctx.audio_processor.transcription
    return ""
