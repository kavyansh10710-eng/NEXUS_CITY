import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
from assets.theme import apply_theme

# ======================
# PAGE CONFIG
# ======================

st.set_page_config(
    page_title="NEXUS Live Analytics",
    layout="wide"
)

apply_theme()

st.title("📊 NEXUS Live Analytics Center")

# Auto Refresh Every 60 Seconds
st_autorefresh(
    interval=60 * 1000,   # 60 seconds
    key="analytics_refresh"
)

st.success("🔄 Live data auto-refreshes every 60 seconds")
col1, col2 = st.columns([4,1])

with col1:
    st.caption(
        f"Last Updated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    )

with col2:
    st.success("🟢 LIVE")

# ======================
# CITY SELECTION
# ======================

cities = {
    "Navsari": (20.9467, 72.9520),
    "Ahmedabad": (23.0225, 72.5714),
    "Mumbai": (19.0760, 72.8777),
}

city = st.selectbox(
    "🏙️ Select City",
    list(cities.keys())
)

lat, lon = cities[city]

# ======================
# WEATHER API (Current + Hourly + Timezone) <--- સુધારો
# ======================

weather_url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={lat}"
    f"&longitude={lon}"
    f"&current=temperature_2m,precipitation"
    f"&hourly=temperature_2m,precipitation"
    f"&timezone=auto"
    f"&forecast_days=2"
)

weather_data = requests.get(weather_url).json()

# ======================
# AIR QUALITY API (Current + Hourly + Timezone) <--- સુધારો
# ======================

air_url = (
    f"https://air-quality-api.open-meteo.com/v1/air-quality"
    f"?latitude={lat}"
    f"&longitude={lon}"
    f"&current=us_aqi,pm2_5"
    f"&hourly=us_aqi,pm2_5"
    f"&timezone=auto"
)

air_data = requests.get(air_url).json()

# ======================
# DATAFRAME (અત્યારના સમયથી આગળના 24 કલાક) <--- સુધારો
# ======================

full_df = pd.DataFrame({
    "Time": pd.to_datetime(weather_data["hourly"]["time"]),
    "Temperature": weather_data["hourly"]["temperature_2m"],
    "Rainfall": weather_data["hourly"]["precipitation"],
    "AQI": air_data["hourly"]["us_aqi"],
    "Pollution": air_data["hourly"]["pm2_5"]
})

# અત્યારના સમય (Current Hour) થી આગળનો 24 કલાકનો લાઇવ ડેટા ફિલ્ટર કરવો
current_hour = datetime.now().replace(minute=0, second=0, microsecond=0)
df = full_df[full_df["Time"] >= current_hour].head(24)

# ======================
# LIVE METRICS (અત્યારનો સાચો લાઇવ ડેટા) <--- સુધારો
# ======================

st.subheader(f"📍 Live Analytics : {city}")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🌡 Temperature",
        f"{weather_data['current']['temperature_2m']} °C"
    )

with col2:
    st.metric(
        "🌧 Rainfall",
        f"{weather_data['current']['precipitation']} mm"
    )

with col3:
    st.metric(
        "🌫 AQI",
        round(air_data['current']['us_aqi'])
    )

with col4:
    st.metric(
        "🏭 Pollution",
        round(air_data['current']['pm2_5'], 1)
    )

st.divider()

# ======================
# TEMPERATURE GRAPH
# ======================

st.subheader("🌡 Temperature Trend (Next 24 Hours)")

temp_fig = px.line(
    df,
    x="Time",
    y="Temperature",
    markers=True
)
temp_fig.update_traces(line_color="orange", line_width=4)
temp_fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="white")
st.plotly_chart(temp_fig, use_container_width=True)

# ======================
# RAINFALL GRAPH
# ======================

st.subheader("🌧 Rainfall Trend (Next 24 Hours)")

rain_fig = px.line(
    df,
    x="Time",
    y="Rainfall",
    markers=True
)
rain_fig.update_traces(line_color="#38BDF8", line_width=4)
rain_fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="white")
st.plotly_chart(rain_fig, use_container_width=True)

# ======================
# AQI GRAPH
# ======================

st.subheader("🌫 AQI Trend (Next 24 Hours)")

aqi_fig = px.line(
    df,
    x="Time",
    y="AQI",
    markers=True
)
aqi_fig.update_traces(line_color="#00BFFF", line_width=4)
aqi_fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="white")
st.plotly_chart(aqi_fig, use_container_width=True)

# ======================
# POLLUTION GRAPH
# ======================

st.subheader("🏭 Pollution Trend (Next 24 Hours)")

pollution_fig = px.line(
    df,
    x="Time",
    y="Pollution",
    markers=True
)
pollution_fig.update_traces(line_color="#22C55E", line_width=4)
pollution_fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="white")
st.plotly_chart(pollution_fig, use_container_width=True)

# ======================
# RAW DATA
# ======================

with st.expander("📄 View Full Live Data"):
    st.dataframe(df, use_container_width=True)
