# 📘 InvestWise Kenya – Streamlit Production Code (Without Colab Setup)

# ------------------------ app.py ------------------------
import streamlit as st
from fetch_data import get_market_data
from stock_data import fetch_nse_stocks
from mmf_data import fetch_mmf_rates
from banks import fetch_bank_rates
from notify import send_email_alert, send_whatsapp_alert
from advisor import advise_user
from logger import save_weekly_log
# from voice_input import voice_input_box
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

st.title('📈 InvestWise Kenya – Real-time Investment Assistant')

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

st.header("📈 Rate Trends")
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
# if st.button("🎤 Use Voice Input"):
#     voice = voice_input_box()
#     if voice:
#         st.success(f"You said: {voice}")
#         st.info(advise_user(voice))
if goal:
    st.success(advise_user(goal))

st.markdown("""
### 💸 Government Tax Info
- Treasury bills & bonds: Withholding tax of **15%** on interest income.
- MMFs: Also subject to **15%** withholding tax.
- Dividends: Subject to **5%** withholding tax.
- Bank savings interest: **15%** withholding.
""")

# ---------------------- voice_input.py ----------------------
# (Voice input temporarily disabled for Streamlit Cloud)

# ---------------------- fetch_data.py ----------------------

def get_market_data():
    import pandas as pd
    return pd.DataFrame({
        'Asset': ['Treasury Bills', 'NSE Stocks', 'Money Market Funds', 'Bank Savings'],
        'Return (%)': [13.8, 9.1, 10.4, 6.2],
        'Risk': ['Low', 'High', 'Moderate', 'Low']
    })

# ---------------------- stock_data.py ----------------------

def fetch_nse_stocks():
    import pandas as pd
    return pd.DataFrame({
        'Company': ['Safaricom', 'KCB', 'Equity', 'EABL'],
        'Price': [16.3, 39.5, 43.2, 165.5],
        '1W Change (%)': [1.2, -0.5, 2.1, 0.3]
    })

# ---------------------- mmf_data.py ----------------------

def fetch_mmf_rates():
    import pandas as pd
    return pd.DataFrame({
        'Fund': ['CIC MMF', 'NCBA MMF', 'Madison MMF'],
        '7-Day Yield (%)': [10.21, 10.04, 9.87],
        'Risk': ['Low', 'Low', 'Low']
    })

# ---------------------- banks.py ----------------------

def fetch_bank_rates():
    import pandas as pd
    return pd.DataFrame({
        'Bank': ['Equity', 'KCB', 'Absa', 'Co-op'],
        'Savings Rate (%)': [6.5, 6.0, 5.8, 5.7]
    })

# ---------------------- notify.py ----------------------

def send_email_alert(to_email, subject, message):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    import os

    email_user = os.getenv("EMAIL_ADDRESS")
    email_pass = os.getenv("EMAIL_PASSWORD")

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))
    text = msg.as_string()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(email_user, email_pass)
        server.sendmail(email_user, to_email, text)


def send_whatsapp_alert(to_number, message):
    from twilio.rest import Client
    import os

    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_NUMBER")

    client = Client(account_sid, auth_token)
    client.messages.create(
        body=message,
        from_='whatsapp:' + from_number,
        to='whatsapp:' + to_number
    )

# ---------------------- advisor.py ----------------------

def advise_user(goal):
    goal = goal.lower()
    if 'save' in goal:
        return '✅ Try Money Market Funds or Treasury Bills.'
    elif 'long' in goal or 'retire' in goal:
        return '📈 Consider a mix of stocks and bonds for long-term growth.'
    elif 'loan' in goal:
        return '💡 Compare interest rates from banks and MMFs before borrowing.'
    else:
        return '🤔 Consider diversifying: low-risk savings + stocks for higher returns.'

# ---------------------- logger.py ----------------------

def save_weekly_log():
    import pandas as pd, os, datetime
    from fetch_data import get_market_data

    data = get_market_data()
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    log_path = "weekly_logs.csv"
    data['Date'] = today

    if os.path.exists(log_path):
        data.to_csv(log_path, mode='a', header=False, index=False)
    else:
        data.to_csv(log_path, index=False)


# ✅ All other required scripts (fetch_data.py, notify.py, etc.) must be included in the same repo for Streamlit Cloud.
# ✅ Also include requirements.txt and .streamlit/config.toml as previously described.

