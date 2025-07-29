# 📘 InvestWise Kenya – Multi-User Streamlit App (Colab Setup with Voice

# 1. Install dependencies
!pip install streamlit pandas requests beautifulsoup4 twilio pyngrok matplotlib seaborn streamlit-webrtc flask ngrok --quiet

# 2. Setup .streamlit config
import os
os.makedirs(".streamlit", exist_ok=True)
with open(".streamlit/config.toml", "w") as f:
    f.write("[server]\nheadless = true\nport = 8501\nenableCORS = false")

# 3. Write all Python app files
code_files = {
    "app.py": '''
import streamlit as st
from fetch_data import get_market_data
from stock_data import fetch_nse_stocks
from mmf_data import fetch_mmf_rates
from banks import fetch_bank_rates
from notify import send_email_alert, send_whatsapp_alert
from advisor import advise_user
from logger import save_weekly_log
from voice_input import voice_input_box
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title='InvestWise Kenya', layout='wide')

# Set background AI-generated image
def set_bg_image():
    bg_url = "https://images.unsplash.com/photo-1607746882042-944635dfe10e"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('{bg_url}');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_image()

st.title('📊 InvestWise Kenya – Real-time Investment Assistant')

save_weekly_log()

st.sidebar.header("🔔 Subscribe for Alerts")
name = st.sidebar.text_input("Name")
user_email = st.sidebar.text_input("Email")
user_phone = st.sidebar.text_input("WhatsApp (+254...)")

if st.sidebar.button("📩 Subscribe Me"):
    new_user = pd.DataFrame([[name, user_email, user_phone]], columns=["Name", "Email", "Phone"])
    new_user.to_csv("subscribers.csv", mode="a", header=not os.path.exists("subscribers.csv"), index=False)
    st.sidebar.success("✅ Subscribed! You’ll receive alerts.")

st.header('📈 Market Overview')
data = get_market_data()
st.dataframe(data)

st.header("📊 Rate Trends")
fig, ax = plt.subplots(figsize=(10, 4))
sns.barplot(x='Asset', y='Return (%)', hue='Risk', data=data, ax=ax)
plt.title("Live Returns Comparison")
st.pyplot(fig)

st.header("📡 Real-Time Investment Options")
tab1, tab2, tab3 = st.tabs(["📈 NSE Stocks", "💰 MMF Yields", "🏦 Bank Rates"])
with tab1:
    st.dataframe(fetch_nse_stocks())
with tab2:
    st.dataframe(fetch_mmf_rates())
with tab3:
    st.dataframe(fetch_bank_rates())

st.header('💡 Smart Investment Advice')
goal = st.text_input("What's your investment goal?")
if st.button("🎤 Use Voice Input"):
    voice = voice_input_box()
    if voice:
        st.success(f"You said: {voice}")
        st.info(advise_user(voice))
if goal:
    st.success(advise_user(goal))

st.markdown("""
### 💸 Government Tax Info
- Treasury bills & bonds: Withholding tax of **15%** on interest income.
- MMFs: Also subject to **15%** withholding tax.
- Dividends: Subject to **5%** withholding tax.
- Bank savings interest: **15%** withholding.
""")
''',

    "voice_input.py": '''
import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode
import whisper
import av

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
'''
}

# Save each file
for name, content in code_files.items():
    with open(name, "w") as f:
        f.write(content)

# 4. Run Streamlit app using ngrok
from pyngrok import ngrok
import threading, time

def run():
    os.system("streamlit run app.py")
threading.Thread(target=run).start()
time.sleep(5)
public_url = ngrok.connect(8501)
print("✅ Your app is live at:", public_url)
