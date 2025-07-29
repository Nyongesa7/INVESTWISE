import streamlit as st
from fetch_data import get_market_data
from advisor import advise_user

st.set_page_config(page_title="InvestWise Kenya", layout="wide")

st.title("📊 InvestWise Kenya – Real-time Investment Assistant")

st.sidebar.header("🔔 Notifications")
email = st.sidebar.text_input("Enter Email")
whatsapp = st.sidebar.text_input("WhatsApp Number (e.g. +2547...)")
if st.sidebar.button("Subscribe"):
    st.success("You’ve been subscribed (mock only).")

st.header("📈 Market Overview (Live Data)")
market_data = get_market_data()
st.dataframe(market_data)

st.header("💡 Smart Investment Advice")
user_goal = st.text_input("Describe your investment goal:")
if user_goal:
    suggestion = advise_user(user_goal)
    st.success(suggestion)
