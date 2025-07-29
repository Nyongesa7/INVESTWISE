# 📘 InvestWise Kenya – Streamlit Production Code (Without Colab Setup)

# ------------------------ app.py ------------------------
import streamlit as st
from fetch_data import get_market_data
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



# ✅ All other required scripts (fetch_data.py, notify.py, etc.) must be included in the same repo for Streamlit Cloud.
# ✅ Also include requirements.txt and .streamlit/config.toml as previously described.

