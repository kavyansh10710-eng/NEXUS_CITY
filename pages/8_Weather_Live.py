import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh
from assets.theme import apply_theme

apply_theme()

st.title("☁️ Weather Intelligence Center")

st_autorefresh(
    interval=60000,
    key="weather_refresh"
)
cities = {
    "Navsari": (20.95, 72.93),
    "Ahmedabad": (23.02, 72.57),
    "Mumbai": (19.07, 72.87),
    "Surat": (21.17, 72.83)
}

city = st.selectbox(
    "Select City",
    list(cities.keys())
)

lat, lon = cities[city]

url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={lat}"
    f"&longitude={lon}"
    f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m,rain"
)

try:
    response = requests.get(url, timeout=10)
    data = response.json()

    current = data["current"]

    temperature = current["temperature_2m"]
    humidity = current["relative_humidity_2m"]
    wind = current["wind_speed_10m"]
    rainfall = current["rain"]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "🌡 Temperature",
        f"{temperature} °C"
    )

    col2.metric(
        "💧 Humidity",
        f"{humidity}%"
    )

    col3.metric(
        "🌬 Wind Speed",
        f"{wind} km/h"
    )

    col4.metric(
        "🌧 Rainfall",
        f"{rainfall} mm"
    )

    st.success(f"✅ Live Weather Data : {city}")

except Exception as e:
    st.error(f"Weather API Error: {e}")
