import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_autorefresh import st_autorefresh
from datetime import datetime

st.title("📊 NEXUS Live Analytics Center")

st.caption(
    f"Last Updated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
)

st_autorefresh(
    interval=60000,
    key="analytics_refresh"
)

st.success("🔄 Live data auto-refreshes every 5 minutes")

# =====================
# CITY SELECTION
# =====================

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

# =====================
# WEATHER API
# =====================

weather_url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={lat}"
    f"&longitude={lon}"
    f"&hourly=temperature_2m,precipitation"
    f"&forecast_days=2"
)

weather_data = requests.get(weather_url).json()

# =====================
# AQI API
# =====================

aqi_url = (
    f"https://air-quality-api.open-meteo.com/v1/air-quality"
    f"?latitude={lat}"
    f"&longitude={lon}"
    f"&hourly=us_aqi"
)

aqi_data = requests.get(aqi_url).json()

# =====================
# DATAFRAME
# =====================

df = pd.DataFrame({
    "Time": weather_data["hourly"]["time"][:24],
    "Temperature": weather_data["hourly"]["temperature_2m"][:24],
    "Rainfall": weather_data["hourly"]["precipitation"][:24],
    "AQI": aqi_data["hourly"]["us_aqi"][:24]
})

# =====================
# LIVE METRICS
# =====================

st.subheader(f"📍 Live Data : {city}")

col1, col2, col3 = st.columns(3)

col1.metric(
    "🌡 Current Temp",
    f"{df['Temperature'].iloc[0]} °C"
)

col2.metric(
    "🌧 Rainfall",
    f"{df['Rainfall'].iloc[0]} mm"
)

col3.metric(
    "🌫 AQI",
    int(df['AQI'].iloc[0])
)

st.divider()

# =====================
# TEMPERATURE GRAPH
# =====================

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

# =====================
# RAINFALL GRAPH
# =====================

st.subheader("🌧 Rainfall Trend")

rain_fig = px.bar(
    df,
    x="Time",
    y="Rainfall"
)

rain_fig.update_traces(
    marker_color="blue"
)

st.plotly_chart(
    rain_fig,
    use_container_width=True
)

# =====================
# AQI GRAPH
# =====================

st.subheader("🌫 AQI Trend")

aqi_fig = px.line(
    df,
    x="Time",
    y="AQI",
    markers=True
)

aqi_fig.update_traces(
    line_color="yellow",
    line_width=4
)

st.plotly_chart(
    aqi_fig,
    use_container_width=True
)

# =====================
# RAW DATA
# =====================

with st.expander("📄 View Live Data Table"):
    st.dataframe(
        df,
        use_container_width=True
    )
