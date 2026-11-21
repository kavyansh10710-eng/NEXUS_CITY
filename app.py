import streamlit as st
import streamlit as st
from logo import show_logo


with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
    
st.set_page_config(
    page_title="NEXUS AI Future Simulator",
    page_icon="🌍",
    layout="wide"
)

show_logo()

<h1 style="color:white;">
🌍 NEXUS ∞
</h1>

<h3 style="color:white;">
Smart City AI Digital Twin Platform
</h3>

<p style="color:white;">
Detect • Predict • Decide
</p>

</div>
""",
unsafe_allow_html=True)
st.subheader("Detect → Predict → Decide")
st.sidebar.markdown("""
# 🤖 NEXUS AI

Status : 🟢 Online

AI Confidence : 98%

Monitoring:

✅ Flood Prediction

✅ Weather Intelligence

✅ AQI Monitoring

✅ Energy Forecasting

✅ City Digital Twin

✅ AI Decision Support
""")

st.markdown("""
### Welcome to NEXUS CITY

NEXUS is an AI-powered Future Simulation Platform.

✅ Flood Prediction

✅ Heatwave Prediction

✅ Air Quality Analysis

✅ Explainable AI

✅ Future Scenario Simulation
""")

st.image(
"https://images.unsplash.com/photo-1486406146926-c627a92ad1ab",
use_container_width=True
)
