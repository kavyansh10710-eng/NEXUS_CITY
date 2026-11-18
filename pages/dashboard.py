import streamlit as st

st.title("📊 Smart City Dashboard")

c1,c2,c3,c4 = st.columns(4)

c1.metric("🌧 Flood Risk","32%","+5%")
c2.metric("🔥 Heatwave","61%","+7%")
c3.metric("💨 Air Quality","Moderate")
c4.metric("⚡ Power Demand","83%")

st.info("Real-time Smart City Overview")
