import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# ======================
# PAGE CONFIG
# ======================

st.set_page_config(
    page_title="NEXUS Live Analytics",
    layout="wide"
)

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

st.caption(
    f"Last Updated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
)

# ======================
# CITY SELECTION
# ======================

cities = {
    "Navsari": (20.9467, 72.9520),
    "Ahmedabad": (23.0225, 72.5714),
    "Mumbai": (19.0760, 72.8777),
    "Bombay": (19.0760, 72.8777)
}

city = st.selectbox(
    "🏙️ Select City",
    list(cities.keys())
)

lat, lon = cities[city]

# ======================
# WEATHER API
# ======================

weather_url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={lat}"
    f"&longitude={lon}"
    f"&hourly=temperature_2m,precipitation"
    f"&forecast_days=2"
)

weather_data = requests.get(weather_url).json()

# ======================
# AIR QUALITY API
# ======================

air_url = (
    f"https://air-quality-api.open-meteo.com/v1/air-quality"
    f"?latitude={lat}"
    f"&longitude={lon}"
    f"&hourly=us_aqi,pm2_5"
)

air_data = requests.get(air_url).json()

# ======================
# DATAFRAME
# ======================

df = pd.DataFrame({
    "Time": weather_data["hourly"]["time"][:24],
    "Temperature": weather_data["hourly"]["temperature_2m"][:24],
    "Rainfall": weather_data["hourly"]["precipitation"][:24],
    "AQI": air_data["hourly"]["us_aqi"][:24],
    "Pollution": air_data["hourly"]["pm2_5"][:24]
})

# ======================
# LIVE METRICS
# ======================

st.subheader(f"📍 Live Analytics : {city}")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🌡 Temperature",
        f"{df['Temperature'].iloc[0]} °C"
    )

with col2:
    st.metric(
        "🌧 Rainfall",
        f"{df['Rainfall'].iloc[0]} mm"
    )

with col3:
    st.metric(
        "🌫 AQI",
        round(df['AQI'].iloc[0])
    )

with col4:
    st.metric(
        "🏭 Pollution",
        round(df['Pollution'].iloc[0], 1)
    )

st.divider()

# ======================
# TEMPERATURE GRAPH
# ======================

st.subheader("🌡 Temperature Trend")

temp_fig = px.line(
    df,
    x="Time",
    y="Temperature",
    markers=True
)

temp_fig.update_traces(
    line_color="orange",
    line_width=4
)

st.plotly_chart(
    temp_fig,
    use_container_width=True
)

# ======================
# RAINFALL GRAPH
# ======================

st.subheader("🌧 Rainfall Trend")

rain_fig = px.line(
    df,
    x="Time",
    y="Rainfall",
    markers=True
)

rain_fig.update_traces(
    line_color="blue",
    line_width=4
)

st.plotly_chart(
    rain_fig,
    use_container_width=True
)

# ======================
# AQI GRAPH
# ======================

st.subheader("🌫 AQI Trend")

aqi_fig = px.line(
    df,
    x="Time",
    y="AQI",
    markers=True
)

aqi_fig.update_traces(
    line_color="#00BFFF",
    line_width=4
)

aqi_fig.update_layout(
    plot_bgcolor="black",
    paper_bgcolor="black",
    font_color="white"
)

st.plotly_chart(
    aqi_fig,
    use_container_width=True
)

# ======================
# POLLUTION GRAPH
# ======================

st.subheader("🏭 Pollution Trend")

pollution_fig = px.line(
    df,
    x="Time",
    y="Pollution",
    markers=True
)

pollution_fig.update_traces(
    line_color="green",
    line_width=4
)

st.plotly_chart(
    pollution_fig,
    use_container_width=True
)

# ======================
# RAW DATA
# ======================

with st.expander("📄 View Full Live Data"):

    st.dataframe(
        df,
        use_container_width=True
    )
