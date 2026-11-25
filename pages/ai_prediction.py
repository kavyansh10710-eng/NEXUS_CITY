import streamlit as st
import randomfrom 
from assets.theme import apply_theme

apply_theme()



st.title("🤖 AI Prediction Engine")

if st.button("Generate Prediction"):

    risk = random.randint(20,95)

    st.metric(
        "Future Risk Score",
        f"{risk}%"
    )

    if risk > 70:
        st.error("High Risk Detected")
    elif risk > 40:
        st.warning("Moderate Risk")
    else:
        st.success("Low Risk")
