import streamlit as st
import streamlit as st
from logo import show_logo


with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
   

st.set_page_config(layout="wide")

show_logo()
    
<div style="
background:linear-gradient(135deg,#00D4FF,#7C3AED);
padding:40px;
border-radius:25px;
text-align:center;
box-shadow:0px 0px 40px rgba(0,212,255,.6);
">



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

Status :  Online

AI Confidence : 98%

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
