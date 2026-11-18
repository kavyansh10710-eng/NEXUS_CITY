import streamlit as st
import folium
import random
from streamlit_folium import st_folium
from folium.plugins import HeatMap

st.set_page_config(layout="wide")

st.title("🛰️ NEXUS Smart City Digital Twin")

# ==========================
# CITY DATA
# ==========================

cities = {
    "Navsari (Gujarat)": {
        "lat": 20.9467,
        "lon": 72.9520,
        "flood": 25,
        "aqi": 70,
        "temp": 31
    },

    "Ahmedabad (Gujarat)": {
        "lat": 23.0225,
        "lon": 72.5714,
        "flood": 40,
        "aqi": 120,
        "temp": 37
    },

    "Mumbai (Maharashtra)": {
        "lat": 19.0760,
        "lon": 72.8777,
        "flood": 75,
        "aqi": 95,
        "temp": 33
    },

    "Bombay (Maharashtra)": {
        "lat": 19.0760,
        "lon": 72.8777,
        "flood": 75,
        "aqi": 95,
        "temp": 33
    }
}

# ==========================
# CITY SELECTOR
# ==========================

city = st.selectbox(
    "🏙️ Select City",
    list(cities.keys())
)

data = cities[city]

lat = data["lat"]
lon = data["lon"]

# ==========================
# AI FUTURE SIMULATOR
# ==========================

st.sidebar.title("⚙️ Future Simulation")

rainfall_change = st.sidebar.slider(
    "🌧 Rainfall Increase (%)",
    0,
    100,
    20
)

population_growth = st.sidebar.slider(
    "👥 Population Growth (%)",
    0,
    100,
    15
)

temp_change = st.sidebar.slider(
    "🔥 Temperature Rise (°C)",
    0,
    10,
    2
)

# ==========================
# RISK SCORE
# ==========================

risk_score = (
    data["flood"]
    + rainfall_change * 0.3
    + population_growth * 0.2
    + temp_change * 2
)

risk_score = round(min(risk_score,100))

# ==========================
# MAP
# ==========================

m = folium.Map(
    location=[lat, lon],
    zoom_start=12,
    tiles=None
)

# Satellite Layer

folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Esri Satellite",
    name="Satellite"
).add_to(m)

# Marker

folium.Marker(
    [lat, lon],
    popup=city,
    tooltip=city,
    icon=folium.Icon(
        color="red",
        icon="info-sign"
    )
).add_to(m)

# ==========================
# HEATMAP
# ==========================

heat_data = []

for i in range(50):

    heat_data.append([
        lat + random.uniform(-0.05,0.05),
        lon + random.uniform(-0.05,0.05),
        random.uniform(0.4,1)
    ])

HeatMap(
    heat_data,
    radius=20
).add_to(m)

# ==========================
# SHOW MAP
# ==========================

st_folium(
    m,
    width=1500,
    height=700
)

# ==========================
# DASHBOARD
# ==========================

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "🌧 Flood Risk",
        f"{data['flood']}%"
    )

with col2:
    st.metric(
        "🌫 AQI",
        data["aqi"]
    )

with col3:
    st.metric(
        "🌡 Temperature",
        f"{data['temp']}°C"
    )

with col4:
    st.metric(
        "🚨 AI Risk Score",
        f"{risk_score}%"
    )

# ==========================
# AI RECOMMENDATION
# ==========================

st.subheader("🤖 AI Recommendation")

if risk_score > 70:

    st.error("""
🔴 HIGH RISK

✅ Expand Water Reservoir

✅ Emergency Flood Planning

✅ Improve Drainage System

✅ Increase Monitoring Sensors

✅ Public Warning System
""")

elif risk_score > 40:

    st.warning("""
🟠 MEDIUM RISK

✅ Continuous Monitoring

✅ Improve City Infrastructure

✅ Water Management Planning
""")

else:

    st.success("""
🟢 LOW RISK

✅ City Conditions Stable

✅ Continue Smart Monitoring
""")

