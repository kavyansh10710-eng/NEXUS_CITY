import streamlit as st
import requests
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from datetime import datetime
from assets.theme import apply_theme

apply_theme()

st.title("📄 NEXUS AI Live PDF Report Generator")

API_KEY = "98d6296f124a940e6ac58e28bbf3625f"

cities = {
    "Navsari": (20.95, 72.93),
    "Vansda": (20.76, 73.37),
    "Surat": (21.17, 72.83),
    "Ahmedabad": (23.02, 72.57),
    "Mumbai": (19.07, 72.87)
}

city = st.selectbox("🏙 Select City", list(cities.keys()))
lat, lon = cities[city]

# 10 મિનિટ (600 સેકન્ડ) સુધી ડેટા કેશ (Cache) રાખશે જેથી API બ્લોક ન થાય
@st.cache_data(ttl=600)
def fetch_live_weather(lat, lon):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    temp, aqi, flood = 30, 85, 20
    
    # પ્રયત્ન 1: OpenWeather API
    w_resp = requests.get(
        f"https://openweathermap.org{lat}&lon={lon}&appid={API_KEY}&units=metric",
        headers=headers,
        timeout=10
    )
    
    if w_resp.status_code == 200 and w_resp.text.strip():
        w_data = w_resp.json()
        temp = int(round(float(w_data["main"]["temp"])))
        rain_mm = float(w_data.get("rain", {}).get("1h", 0))
        humidity = int(w_data["main"]["humidity"])
        flood = min(100, int((humidity * 0.25) + (rain_mm * 15)))
        
        # AQI ડેટા
        a_resp = requests.get(
            f"https://openweathermap.org{lat}&lon={lon}&appid={API_KEY}",
            headers=headers,
            timeout=10
        )
        if a_resp.status_code == 200 and a_resp.text.strip():
            a_data = a_resp.json()
            aqi_idx = a_data["list"]["main"]["aqi"]
            aqi_map = {1: 35, 2: 75, 3: 130, 4: 210, 5: 320}
            aqi = aqi_map.get(aqi_idx, 95)
            
        return True, temp, aqi, flood, "OpenWeather"
    
    # પ્રયત્ન 2: જો OpenWeather માં એરર આવે તો Open-Meteo બેકઅપ
    om_resp = requests.get(
        f"https://open-meteo.com{lat}&longitude={lon}&current=temperature_2m,rain",
        headers=headers,
        timeout=10
    )
    if om_resp.status_code == 200 and om_resp.text.strip():
        om_data = om_resp.json()
        temp = int(round(float(om_data["current"]["temperature_2m"])))
        rain_mm = float(om_data["current"]["rain"])
        flood = min(100, int(15 + (rain_mm * 15)))
        return True, temp, 85, flood, "Open-Meteo"

    return False, temp, aqi, flood, f"Status: {w_resp.status_code} | Msg: {w_resp.text[:100]}"

# ડેટા લાવવાનો પ્રયત્ન કરો
try:
    is_live, live_temp, live_aqi, live_flood_risk, source_info = fetch_live_weather(lat, lon)
except Exception as e:
    is_live, live_temp, live_aqi, live_flood_risk, source_info = False, 30, 85, 20, str(e)

if is_live:
    st.success(f"🟢 Live Real-Time Data Loaded for **{city}** via {source_info}! (Temp: {live_temp}°C | AQI: {live_aqi})")
else:
    st.error(f"⚠️ API Debug Info: {source_info}")
    st.warning("⚠️ Could not fetch live data. Showing default values.")

# શહેર બદલતા જ સ્લાઈડર નવા લાઈવ ડેટા પર અપડેટ થશે
flood_risk = st.slider("🌊 Flood Risk (%)", 0, 100, live_flood_risk, key=f"flood_{city}")
aqi = st.slider("🌫 Air Quality Index (AQI)", 0, 500, live_aqi, key=f"aqi_{city}")
temperature = st.slider("🌡 Temperature (°C)", 0, 50, live_temp, key=f"temp_{city}")

if st.button("📄 Generate PDF Report"):

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)

    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(50, 800, "NEXUS AI Future Simulator")

    pdf.setFont("Helvetica", 14)
    pdf.drawString(50, 770, "Smart City Live Risk Assessment Report")
    pdf.line(50, 760, 550, 760)

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 720, f"City : {city}")
    pdf.drawString(50, 690, f"Flood Risk : {flood_risk}%")
    pdf.drawString(50, 660, f"Air Quality Index (AQI) : {aqi}")
    pdf.drawString(50, 630, f"Temperature : {temperature} °C")
    pdf.drawString(50, 600, f"Report Date & Time : {datetime.now().strftime('%d-%m-%Y %I:%M %p')}")

    pdf.line(50, 570, 550, 570)

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, 530, "AI Risk Analysis & Recommendations")
    pdf.setFont("Helvetica", 12)

    if flood_risk >= 70:
        status = "HIGH FLOOD RISK"
        recommendation = (
            "1. Expand Water Reservoirs & Open Dam Gates.\n"
            "2. Deploy Emergency Rescue Teams immediately.\n"
            "3. Activate Public Flood Warning System."
        )
    elif flood_risk >= 40:
        status = "MEDIUM FLOOD RISK"
        recommendation = (
            "1. Monitor River and Dam Water Levels closely.\n"
            "2. Clear Drainage Infrastructure in low-lying areas."
        )
    else:
        status = "LOW FLOOD RISK"
        recommendation = (
            "1. Current water and weather conditions are stable.\n"
            "2. Continue routine smart city monitoring."
        )

    if aqi > 150:
        aqi_advice = "Air Quality Alert: Advise citizens to wear N95 masks outdoors."
    elif aqi > 100:
        aqi_advice = "Air Quality Note: Sensitive groups should limit outdoor exertion."
    else:
        aqi_advice = "Air Quality Status: Air quality is safe for normal activities."

    pdf.drawString(50, 495, f"Overall Status : {status}")
    pdf.drawString(50, 470, f"{aqi_advice}")

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, 435, "Action Plan:")

    pdf.setFont("Helvetica", 11)
    text = pdf.beginText(50, 415)
    text.textLines(recommendation)
    pdf.drawText(text)

    pdf.line(50, 150, 550, 150)
    pdf.setFont("Helvetica-Oblique", 10)
    pdf.drawString(50, 130, "Generated by NEXUS Smart City AI Platform | Real-Time Intelligence")

    pdf.save()
    pdf_data = buffer.getvalue()

    st.success("✅ Live PDF Report Generated Successfully!")

    st.download_button(
        label="⬇ Download PDF Report",
        data=pdf_data,
        file_name=f"{city}_NEXUS_Live_Report.pdf",
        mime="application/pdf"
    )
