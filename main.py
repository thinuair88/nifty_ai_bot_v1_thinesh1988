import streamlit as st

st.set_page_config(page_title="NIFTY AI Bot", layout="centered")

st.title("📈 NIFTY Futures AI Bot (Demo)")

# Simulated Signal Output
st.markdown("### ✅ Signal: **BUY**")
st.metric(label="NIFTY Price", value="₹22,540")
st.metric(label="Sentiment", value="Bullish 🟢")
st.metric(label="PCR (ATM)", value="1.42")

st.markdown("---")
st.markdown("🧠 This is a demo dashboard for AI-based trading bot using news sentiment and option chain data.")