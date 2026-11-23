import streamlit as st
from logo import show_logo

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="NEXUS ∞ AI Future Simulator",
    page_icon="assets/favicon.png",
    layout="wide"
)

# -----------------------------
# LOAD CSS
# -----------------------------
def load_css():
    try:
        with open("assets/style.css", "r", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    except:
        pass

load_css()

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🤖 NEXUS ∞")
st.sidebar.markdown("---")

st.sidebar.success("🟢 AI Core Online")

st.sidebar.metric(
    "AI Confidence",
    "98%"
)

st.sidebar.metric(
    "Prediction Accuracy",
    "94%"
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
### Active Modules

🌦️ Weather AI

🌊 Flood Prediction

🔥 Heatwave Analysis

🌫️ AQI Monitoring

⚡ Energy Forecast

🏙️ Smart City Twin
""")

# -----------------------------
# LOGO
# -----------------------------
show_logo()

# -----------------------------
# HERO SECTION
# -----------------------------
st.markdown("""
<div style="text-align:center;padding:30px;">
<h1 style="color:#00E5FF;">
NEXUS ∞ AI Future Simulator
</h1>
<p style="font-size:20px;">
Detect → Predict → Decide
</p>

</div>
""", unsafe_allow_html=True)

# -----------------------------
# HERO IMAGE
# -----------------------------
st.image(
    "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1920",
    use_container_width=True
)

# -----------------------------
# DASHBOARD CARDS
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🌦️ Temperature",
        "34°C",
        "+2°C"
    )

with col2:
    st.metric(
        "🌊 Flood Risk",
        "Medium",
        "+5%"
    )

with col3:
    st.metric(
        "🌫️ AQI",
        "78",
        "-3"
    )

with col4:
    st.metric(
        "⚡ Energy Demand",
        "82%",
        "+7%"
    )

# -----------------------------
# MAIN CONTENT
# -----------------------------
st.markdown("## 🚀 Welcome to NEXUS CITY")

st.markdown("""
### AI Powered Smart City Command Center

NEXUS is an advanced Decision Intelligence Platform.

✅ Flood Prediction

✅ Heatwave Forecasting

✅ Air Quality Monitoring

✅ Weather Intelligence

✅ Energy Consumption Analytics

✅ Explainable AI

✅ Future Scenario Simulation

✅ Real-Time Risk Assessment

✅ Smart City Digital Twin
""")

# -----------------------------
# AI MODULES
# -----------------------------
st.markdown("## 🧠 Core AI Modules")

c1, c2 = st.columns(2)

with c1:
    st.info("""
    🌊 Flood Prediction Engine

    • Rainfall Analysis

    • River Level Monitoring

    • Risk Score Generation

    • Early Warning Alerts
    """)

with c2:
    st.info("""
    🌫️ Environment Intelligence

    • AQI Prediction

    • Pollution Detection

    • Heatwave Forecast

    • Weather Analytics
    """)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")

