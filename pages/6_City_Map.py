# =========================
# NEXUS ∞ SMART CITY MAP
# =========================

import streamlit as st
import pandas as pd
import folium
import requests

from folium.features import DivIcon
from streamlit_folium import st_folium
from streamlit_autorefresh import st_autorefresh
from assets.theme import apply_theme

apply_theme()

# =========================
# PAGE CONFIG
# =========================

from PIL import Image

favicon = Image.open("assets/favicon.png")

st.set_page_config(
    page_title="NEXUS ∞ Smart City Map",
    page_icon=favicon,
    layout="wide"
)

# =========================
# OPENWEATHER API KEY
# =========================

API_KEY = "98d6296f124a940e6ac58e28bbf3625f"

# =========================
# AUTO REFRESH (5 MIN)
# =========================

st_autorefresh(
    interval=300000,
    key="city_refresh"
)

# =========================
# TITLE
# =========================

st.title("🛰️ NEXUS ∞ Smart City Map")

st.info(
    "🌡️ Live Weather • 🌧️ Rainfall • 💨 Wind • 🫁 AQI • 🔄 Refresh Every 5 Minutes"
)

# =========================
# CITY DATA
# =========================

cities = [
    ["Ahmedabad",23.0225,72.5714],
    ["Surat",21.1702,72.8311],
    ["Vadodara",22.3072,73.1812],
    ["Rajkot",22.3039,70.8022],
    ["Mumbai",19.0760,72.8777],
    ["Pune",18.5204,73.8567],
    ["Nagpur",21.1458,79.0882],
    ["Delhi",28.6139,77.2090],
    ["Noida",28.5355,77.3910],
    ["Gurugram",28.4595,77.0266],
    ["Bengaluru",12.9716,77.5946],
    ["Chennai",13.0827,80.2707],
    ["Hyderabad",17.3850,78.4867],
    ["Kolkata",22.5726,88.3639],
    ["Jaipur",26.9124,75.7873],
    ["Lucknow",26.8467,80.9462],
    ["Indore",22.7196,75.8577],
    ["Bhopal",23.2599,77.4126],
    ["Patna",25.5941,85.1376],
    ["Kochi",9.9312,76.2673],
    ["Srinagar",34.0837,74.7973],
    ["Guwahati",26.1445,91.7362]
]

df = pd.DataFrame(
    cities,
    columns=["City","Latitude","Longitude"]
)

# =========================
# WEATHER FUNCTION
# =========================

@st.cache_data(ttl=300)
def get_weather_data(lat, lon):

    try:

        weather_url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?lat={lat}"
            f"&lon={lon}"
            f"&appid={API_KEY}"
            f"&units=metric"
        )

        weather_response = requests.get(
            weather_url,
            timeout=10
        )

        weather = weather_response.json()

        if weather_response.status_code != 200:
            return None

        temp = weather["main"]["temp"]
        humidity = weather["main"]["humidity"]
        wind = weather["wind"]["speed"]

        condition = weather["weather"][0]["main"]

        rainfall = 0

        if "rain" in weather:
            rainfall = weather["rain"].get("1h", 0)

        air_url = (
            f"https://api.openweathermap.org/data/2.5/air_pollution"
            f"?lat={lat}"
            f"&lon={lon}"
            f"&appid={API_KEY}"
        )

        air_response = requests.get(
            air_url,
            timeout=10
        )

        air_data = air_response.json()

        aqi = air_data["list"][0]["main"]["aqi"]

        return {
            "temp": round(temp,1),
            "humidity": humidity,
            "wind": round(wind,1),
            "weather": condition,
            "rainfall": rainfall,
            "aqi": aqi
        }

    except:
        return None


# =========================
# CITY SEARCH
# =========================

selected_city = st.selectbox(
    "🔍 Search City",
    ["All Cities"] + df["City"].tolist()
)

if selected_city == "All Cities":

    map_center = [22.5937, 78.9629]
    zoom = 5

else:

    selected_row = df[
        df["City"] == selected_city
    ].iloc[0]

    map_center = [
        selected_row["Latitude"],
        selected_row["Longitude"]
    ]

    zoom = 10

# =========================
# GOOGLE HYBRID MAP
# =========================

m = folium.Map(
    location=map_center,
    zoom_start=zoom,
    tiles=None,
    control_scale=True
)

folium.TileLayer(
    tiles="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
    attr="Google",
    name="Google Hybrid"
).add_to(m)

# =========================
# ANIMATION CSS
# =========================

m.get_root().html.add_child(
    folium.Element(
        """
<style>

.pulse-marker{
    width:18px;
    height:18px;
    border-radius:50%;
    position:relative;
}

.pulse-marker:after{
    content:'';
    width:18px;
    height:18px;
    border-radius:50%;
    position:absolute;
    left:0;
    top:0;
    animation:pulse 2s infinite;
}

@keyframes pulse{

    0%{
        transform:scale(1);
        opacity:1;
    }

    100%{
        transform:scale(4);
        opacity:0;
    }
}

</style>
"""
    )
)

# =========================
# MARKERS
# =========================

for _, row in df.iterrows():

    data = get_weather_data(
        row["Latitude"],
        row["Longitude"]
    )

    if data is None:

        data = {
            "temp":"--",
            "humidity":"--",
            "wind":"--",
            "weather":"Offline",
            "rainfall":"--",
            "aqi":0
        }

    aqi = data["aqi"]

    marker_color = "#00ffff"

    if aqi == 1:
        marker_color = "#00ff00"

    elif aqi == 2:
        marker_color = "#ccff00"

    elif aqi == 3:
        marker_color = "#ffff00"

    elif aqi == 4:
        marker_color = "#ff8800"

    elif aqi == 5:
        marker_color = "#ff0000"

    popup = f"""
    <div style="width:260px">

    <h3 style="color:{marker_color}">
    🏙️ {row["City"]}
    </h3>

    <hr>

    🌡️ Temperature: {data["temp"]} °C<br>
    ☁️ Weather: {data["weather"]}<br>
    💧 Humidity: {data["humidity"]}%<br>
    🌧️ Rainfall: {data["rainfall"]} mm<br>
    💨 Wind Speed: {data["wind"]} m/s<br>
    🫁 AQI: {data["aqi"]}<br><br>

    ✅ Live Monitoring<br>

    </div>
    """

    folium.Marker(
        location=[
            row["Latitude"],
            row["Longitude"]
        ],
        tooltip=row["City"],
        popup=folium.Popup(
            popup,
            max_width=320
        ),
        icon=DivIcon(
            html=f"""
            <div class='pulse-marker'
            style='
            background:{marker_color};
            box-shadow:0 0 20px {marker_color};
            '></div>
            """
        )
    ).add_to(m)

# =========================
# MAP DISPLAY
# =========================

st_folium(
    m,
    use_container_width=True,
    height=800
)

st.success(
    f"✅ Monitoring {len(df)} Major Indian Cities"
)
<br>
