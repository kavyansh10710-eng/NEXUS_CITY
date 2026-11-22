import streamlit as st
from logo import show_logo

# ------------------------
# Page Config (સૌથી પહેલાં)
# ------------------------
st.set_page_config(
    page_title="NEXUS ∞ Smart City AI",
    page_icon="🏙️",
    layout="wide"
)

# ------------------------
# Load CSS
# ------------------------
def load_css():
    with open("assets/style.css", "r") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ------------------------
# Sidebar Theme Toggle
# ------------------------
light_mode = st.sidebar.toggle(
    "☀️ Light Mode",
    value=False
)

# ------------------------
# Logo
# ------------------------
show_logo()

# ------------------------
# Sidebar
# ------------------------
st.sidebar.markdown("""
# 🤖 NEXUS AI

🟢 Status : Online

🎯 AI Confidence : 98%
""")

# ------------------------
# Hero Section
# ------------------------
st.markdown("""
<div class="hero-title">
NEXUS ∞
</div>

<div class="hero-subtitle">
Award-Winning Smart City AI Platform
</div>
""", unsafe_allow_html=True)

# ------------------------
# Welcome Section
# ------------------------
st.markdown("""
### 🌍 Welcome to NEXUS CITY

NEXUS is an AI-Powered Digital Platform.

✅ Flood Prediction

✅ Heatwave Prediction

✅ Air Quality Analysis

✅ Weather Intelligence

✅ Energy Forecasting

✅ Explainable AI

✅ Future Scenario Simulation
""")

# ------------------------
# Hero Image
# ------------------------
st.image(
    "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1920",
    use_container_width=True
)

# ------------------------
# KPI Cards
# ------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="glass-card">
        <h3>🌊 Flood Risk</h3>
        <h1>42%</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card">
        <h3>🌡 Temperature</h3>
        <h1>34°C</h1>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="glass-card">
        <h3>🏭 AQI</h3>
        <h1>78</h1>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="glass-card">
        <h3>⚡ Power</h3>
        <h1>84 MW</h1>
    </div>
    """, unsafe_allow_html=True)
