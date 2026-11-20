import streamlit as st
import random

st.title("☁️ Smart Weather Monitoring")
st.subheader(
"☁️ Weather Intelligence Center"
)
cities = [
    "Navsari",
    "Ahmedabad",
    "Mumbai",
    "Bombay"
]

city = st.selectbox(
    "Select City",
    cities
)

temperature = random.randint(25,40)
humidity = random.randint(40,95)
wind = random.randint(5,30)

col1,col2,col3 = st.columns(3)

col1.metric(
    "🌡 Temperature",
    f"{temperature}°C"
)

col2.metric(
    "💧 Humidity",
    f"{humidity}%"
)

col3.metric(
    "🌬 Wind Speed",
    f"{wind} km/h"
)

st.info(f"Current Weather Status : {city}")
