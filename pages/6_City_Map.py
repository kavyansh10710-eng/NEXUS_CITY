import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")

st.title("🛰️ City Map")

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
# SIDEBAR SIMULATION
# ==========================

st.sidebar.title("⚙️ Future Simulation")

rainfall_change = st.sidebar.slider(
    "🌧 Rainfall Increase (%)",
    0, 100, 20
)

population_growth = st.sidebar.slider(
    "👥 Population Growth (%)",
    0, 100, 15
)

temp_change = st.sidebar.slider(
    "🔥 Temperature Rise (°C)",
    0, 10, 2
)

# ==========================
# AI RISK SCORE
# ==========================

risk_score = (
    data["flood"]
    + rainfall_change * 0.3
    + population_growth * 0.2
    + temp_change * 2
)

risk_score = min(round(risk_score), 100)

# ==========================
# RISK COLOR
# ==========================

if risk_score >= 70:
    zone_color = "red"
elif risk_score >= 40:
    zone_color = "orange"
else:
    zone_color = "green"

# ==========================
# CREATE MAP
# ==========================

m = folium.Map(
    location=[lat, lon],
    zoom_start=12,
    tiles=None
)

# ==========================
# SATELLITE VIEW
# ==========================

folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Esri Satellite",
    name="Satellite"
).add_to(m)

# ==========================
# CITY MARKER
# ==========================

folium.CircleMarker(
    location=[lat, lon],
    radius=10,
    popup=city,
    tooltip=city,
    color=zone_color,
    fill=True,
    fill_color=zone_color,
    fill_opacity=1
).add_to(m)

# ==========================
# RISK ZONE
# ==========================

folium.Circle(
    location=[lat, lon],
    radius=3000,
    color=zone_color,
    fill=True,
    fill_color=zone_color,
    fill_opacity=0.20,
    popup=f"Risk Score: {risk_score}%"
).add_to(m)

# ==========================
# MAP DISPLAY
# ==========================

st_folium(
    m,
    width=1500,
    height=750,
    returned_objects=[]
)

# ==========================
# CITY METRICS
# ==========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🌊 Flood Risk",
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

if risk_score >= 70:

    st.error("""
🔴 HIGH RISK

✅ Expand Water Reservoir

✅ Improve Drainage

✅ Activate Emergency Teams

✅ Continuous Monitoring
""")

elif risk_score >= 40:

    st.warning("""
🟠 MEDIUM RISK

✅ Monitor Environment

✅ Upgrade Infrastructure

✅ Prepare Backup Resources
""")

else:

    st.success("""
🟢 LOW RISK

✅ Stable Conditions

✅ Continue Monitoring

✅ Maintain Smart Infrastructure
""")
