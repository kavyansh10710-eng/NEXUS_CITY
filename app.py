import streamlit as st

with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
import streamlit as st

st.set_page_config(
    page_title="NEXUS AI Future Simulator",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 NEXUS ∞ AI Future Simulator")
st.subheader("Detect → Predict → Decide")

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
