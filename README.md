# investwise
# 📈 InvestWise Kenya

**InvestWise Kenya** is a real-time, multi-user investment advisory app designed for Kenyan users. It aggregates data from Treasury Bills, NSE stocks, Money Market Funds (MMFs), and bank savings accounts to provide personalized investment advice, charts, alerts, and insights.

---

## 🌟 Features

* ✅ Real-time financial data (T-Bills, NSE, MMFs, Banks)
* 📊 Interactive charts comparing risk and returns
* 💬 Email + WhatsApp investment alerts (Twilio-enabled)
* 🤖 Smart investment advice based on user goals
* 🔔 User subscription with auto logging
* 📁 Weekly logs saved to CSV for tracking

---

## 🛠 Installation

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/investwise.git
cd investwise
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables (for alerts)

Create a `.streamlit/secrets.toml` file:

toml
EMAIL_ADDRESS = "johnnyongesa7@gmail.com"
EMAIL_PASSWORD = "your-app-password"
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth"
TWILIO_NUMBER = "your_whatsapp_number"




🚀 Run Locally

bash
streamlit run app.py
```



☁️ Deploy on Streamlit Cloud

1. Push to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your repo
4. Set `app.py` as the entry point
5. Add your email/Twilio credentials to the **Secrets** tab



## 📁 Project Structure

```
investwise/
├── app.py                 # Main Streamlit app
├── fetch_data.py          # Static market data
├── stock_data.py          # NSE stock mock data
├── mmf_data.py            # MMF rate mock data
├── banks.py               # Bank savings mock data
├── notify.py              # Email & WhatsApp alert logic
├── advisor.py             # Smart advice generator
├── logger.py              # Weekly CSV logger
├── requirements.txt
└── .streamlit/
    ├── config.toml        # Streamlit config
    └── secrets.toml       # Your API s
🧠 Example Use Case

1. A user logs in and describes a goal: "I want to save for a house."
2. App recommends low-risk assets like MMFs and T-Bills.
3. Weekly charts show returns for various assets.
4. User subscribes to WhatsApp + Email alerts for new CBK rates.


 🙌 Credits

Made with ❤️ for Kenyan investors by @nyongesa7
