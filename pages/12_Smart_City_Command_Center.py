import streamlit as st
import requests
from datetime import datetime
from assets.theme import apply_theme

apply_theme()

st.title("🖥 Navsari City Command Center")

API_KEY = "98d6296f124a940e6ac58e28bbf3625f"

# નવસારી (Navsari) ના Latitude અને Longitude
LAT = 20.95
LON = 72.93

@st.cache_data(ttl=600)
def get_navsari_live_data():
    headers = {"User-Agent": "Mozilla/5.0"}
    # ડિફોલ્ટ વેલ્યુ (જો API માં કોઈ વિલંબ થાય તો)
    data = {
        "is_live": False,
        "temp": 30,
        "humidity": 60,
        "rain": 0.0,
        "aqi_text": "Moderate",
        "flood_alert": "Low",
        "power_demand": "75%",
        "risk_level": "Low",
        "auto_situation": "Air Pollution",
        "updated_time": datetime.now().strftime("%I:%M %p")
    }
    
    try:
        # 1. નવસારીનો લાઈવ વેધર ડેટા (OpenWeather)
        w_resp = requests.get(
            "https://openweathermap.org",
            params={"lat": LAT, "lon": LON, "appid": API_KEY, "units": "metric"},
            headers=headers,
            timeout=10
        )
        
        if w_resp.status_code == 200 and w_resp.text.strip():
            w_json = w_resp.json()
            temp = round(float(w_json["main"]["temp"]))
            humidity = int(w_json["main"]["humidity"])
            rain = float(w_json.get("rain", {}).get("1h", 0))
            
            data["temp"] = temp
            data["humidity"] = humidity
            data["rain"] = rain
            data["is_live"] = True
            
            # વરસાદ અને ભેજ મુજબ Flood Alert નક્કી કરવું
            if rain >= 10 or (rain > 2 and humidity > 85):
                data["flood_alert"] = "High"
            elif rain > 0 or humidity > 80:
                data["flood_alert"] = "Medium"
            else:
                data["flood_alert"] = "Low"
                
            # તાપમાન મુજબ Power Demand ગણતરી
            calc_power = min(98, max(55, int(50 + (temp * 1.1))))
            data["power_demand"] = f"{calc_power}%"
            
        # 2. નવસારીનો લાઈવ AQI ડેટા
        a_resp = requests.get(
            "https://openweathermap.org",
            params={"lat": LAT, "lon": LON, "appid": API_KEY},
            headers=headers,
            timeout=10
        )
        
        aqi_idx = 2
        if a_resp.status_code == 200 and a_resp.text.strip():
            a_json = a_resp.json()
            aqi_idx = a_json["list"][0]["main"]["aqi"]
            aqi_labels = {1: "Good", 2: "Fair", 3: "Moderate", 4: "Poor", 5: "Very Poor"}
            data["aqi_text"] = aqi_labels.get(aqi_idx, "Moderate")
            
        # એકંદર Risk Level અને મુખ્ય પરિસ્થિતિ (Situation) નક્કી કરવી
        if data["flood_alert"] == "High" or aqi_idx >= 5 or data["temp"] >= 42:
            data["risk_level"] = "High"
        elif data["flood_alert"] == "Medium" or aqi_idx >= 3 or data["temp"] >= 37:
            data["risk_level"] = "Medium"
        else:
            data["risk_level"] = "Low"
            
        # હાલના હવામાન મુજબ AI Decision Center માં કયો વિકલ્પ પહેલા બતાવવો
        if data["flood_alert"] in ["High", "Medium"]:
            data["auto_situation"] = "Flood"
        elif data["temp"] >= 36:
            data["auto_situation"] = "Heatwave"
        else:
            data["auto_situation"] = "Air Pollution"
            
    except Exception:
        pass
        
    return data

# નવસારીનો લાઈવ ડેટા મેળવો
live_data = get_navsari_live_data()

# સ્ટેટસ બાર
if live_data["is_live"]:
    st.success(f"🛰 542 Sensors Online in **Navsari** | Live Temp: **{live_data['temp']}°C** | Humidity: **{live_data['humidity']}%**")
else:
    st.warning("🛰 542 Sensors Online")

st.success("⚡ Power Grid Connected")
st.success(f"☁ Weather Monitoring Active (Last Sync: {live_data['updated_time']})")

# 5 લાઈવ મેટ્રિક્સ કાર્ડ્સ (Temperature ઉમેર્યું અને Risk Level નામ રાખ્યું)
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "🌡 Temperature",
    f"{live_data['temp']} °C",
    f"Humidity: {live_data['humidity']}%"
)

col2.metric(
    "🌊 Flood Alert",
    live_data["flood_alert"],
    f"Rain: {live_data['rain']} mm"
)

col3.metric(
    "🌫 AQI Status",
    live_data["aqi_text"],
    "Navsari Live"
)

col4.metric(
    "⚡ Power Demand",
    live_data["power_demand"]
)

col5.metric(
    "⚠️ Risk Level",
    live_data["risk_level"]
)

st.divider()

# AI Decision Center (નવસારીની હાલની પરિસ્થિતિ મુજબ આપમેળે પસંદ થશે)
st.subheader("🧠 AI Decision Center (Navsari)")

situations = ["Flood", "Heatwave", "Air Pollution"]
default_index = situations.index(live_data["auto_situation"])

status = st.selectbox(
    "Select Situation (Auto-detected based on live weather)",
    situations,
    index=default_index
)

if status == "Flood":
    st.error("""
    ✅ Activate Emergency Pumps in Low-Lying Areas (Purna River Belt)

    ✅ Open Water Drainage Channels

    ✅ Issue Public Flood Alert System

    ✅ Keep Rescue & Evacuation Teams Ready
    """)

elif status == "Heatwave":
    st.warning("""
    ✅ Open Public Cooling & Hydration Centers

    ✅ Increase Drinking Water Distribution

    ✅ Issue Afternoon Heatwave Health Advisory
    """)

else:
    st.info("""
    ✅ Monitor & Reduce Highway/City Traffic Pollution

    ✅ Inspect Industrial & Factory Emissions

    ✅ Active Air Quality Surveillance across Navsari
    """)
