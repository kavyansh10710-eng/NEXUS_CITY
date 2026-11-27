import streamlit as st
import requests
import base64
from logo import show_logo
from assets.theme import apply_theme

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
# LOGO & Theme
# -----------------------------
apply_theme()

# -----------------------------
# SET BACKGROUND IMAGE (GitHub File: assets/hero_banner.png)
# -----------------------------
def set_bg_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: linear-gradient(rgba(10, 15, 30, 0.3), rgba(10, 15, 30, 0.3)), url("data:image/png;base64,{encoded}") !important;
                background-size: cover !important;
                background-position: center !important;
                background-repeat: no-repeat !important;
                background-attachment: fixed !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.warning("⚠️ assets/hero_banner.png ફાઇલ મળી નથી. GitHub માં ફાઇલનું નામ અને ફોલ્ડર ચેક કરો.")

# તમારી GitHub ફાઇલનો પાથ
set_bg_image("assets/hero_banner.png")

show_logo()

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

# -----------------------------
# VANSDA LIVE WEATHER
# -----------------------------
API_KEY = "98d6296f124a940e6ac58e28bbf3625f"

LAT = 20.758
LON = 73.367

try:
    weather_url = (
        f"https://openweathermap.org?"
        f"lat={LAT}"
        f"&lon={LON}"
        f"&appid={API_KEY}"
        f"&units=metric"
    )

    weather_data = requests.get(
        weather_url,
        timeout=10
    ).json()

    temp = round(weather_data["main"]["temp"])
    humidity = weather_data["main"]["humidity"]
    weather = weather_data["weather"][0]["main"]
    wind = round(weather_data["wind"]["speed"], 1)

    # AQI DATA
    aqi_url = (
        f"https://openweathermap.org?"
        f"lat={LAT}"
        f"&lon={LON}"
        f"&appid={API_KEY}"
    )

    aqi_data = requests.get(
        aqi_url,
        timeout=10
    ).json()

    aqi = aqi_data["list"][0]["main"]["aqi"]

except:
    temp = "N/A"
    humidity = "N/A"
    weather = "N/A"
    wind = "N/A"
    aqi = "N/A"

# -----------------------------
# HERO SECTION (New Title + Neon Gradient)
# -----------------------------
st.markdown("""
<div style="text-align:center; padding:25px 10px;">
    <h1 style="
        font-size: 48px;
        font-weight: 800;
        background: linear-gradient(90deg, #00F2FE 0%, #4FACFE 45%, #C084FC 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 0px 25px rgba(0, 242, 254, 0.35);
        margin-bottom: 8px;
        letter-spacing: 1.5px;
    ">
        SMART CITY COMMAND CENTER
    </h1>
    <p style="
        font-size: 20px;
        font-weight: 500;
        color: #E0F2FE;
        letter-spacing: 3px;
        text-shadow: 0px 0px 10px rgba(0, 229, 255, 0.6);
    ">
        DETECT → PREDICT → DECIDE
    </p>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# LIVE WEATHER CARDS
# -----------------------------
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "🌡️ Temperature",
        f"{temp}°C"
    )

with col2:
    st.metric(
        "💧 Humidity",
        f"{humidity}%"
    )

with col3:
    st.metric(
        "☁️ Weather",
        weather
    )

with col4:
    st.metric(
        "🌬️ Wind",
        f"{wind} m/s"
    )

with col5:
    aqi_status = {
        1: "Good",
        2: "Fair",
        3: "Moderate",
        4: "Poor",
        5: "Very Poor"
    }

    st.metric(
        "🌫️ AQI",
        aqi_status.get(aqi, "N/A")
    )

# -----------------------------
# MAIN CONTENT
# -----------------------------
st.markdown("## 🚀 Welcome to NEXUS ∞ ")

st.markdown("""
### AI Powered Smart City Command Center

NEXUS ∞ is an advanced Decision Intelligence Platform.

✅ Flood Prediction

✅ Air Quality Monitoring

✅ Weather Intelligence

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
    st.markdown("""
<div class="ai-card">
<h3>🌊 Flood Prediction Engine</h3>
• Rainfall Analysis<br>
• Risk Score Generation<br>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
