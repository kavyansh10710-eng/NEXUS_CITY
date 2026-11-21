import streamlit as st


# Page Setup
st.set_page_config(
    page_title="NEXUS ∞",
    layout="wide",
    page_icon="🌍"
)
# NEXUS INFINITY THEME SWITCHER

light_mode = st.sidebar.toggle(
    "☀️ Light Mode",
    value=False
)

# CSS Load
with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# Animated Logo
show_logo()

# Sidebar
st.sidebar.markdown("""
# 🤖 NEXUS AI

🟢 Status : Online

🎯 AI Confidence : 98%

### Monitoring

✅ Flood Prediction
✅ Weather Intelligence
✅ AQI Monitoring
✅ Energy Forecasting
✅ City Digital Twin
✅ AI Decision Support
""")

# Welcome Section
st.markdown("""
### Welcome to NEXUS CITY

NEXUS is an AI-Powered Smart City Digital Twin Platform.

✅ Flood Prediction

✅ Heatwave Prediction

✅ Air Quality Analysis

✅ Weather Intelligence

✅ Energy Forecasting

✅ Explainable AI

✅ Future Scenario Simulation
""")

# Hero Image
st.image(
    "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1920",
    use_container_width=True
)
