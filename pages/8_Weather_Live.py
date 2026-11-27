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
    
    # AI Decision Center (નવસારીની હાલની પરિસ્થિતિ મુજબ આપમેળે પસંદ થશે)
st.subheader("🧠 AI Decision Center (Navsari)")

situations = ["Drought", "Heatwave","Typhoon","Air Pollution"]
default_index = situations.index(live_data["auto_situation"])

status = st.selectbox(
    "Select Situation (Auto-detected based on live weather)",
    situations,
    index=default_index
)

if status == "Drought":
    st.error("""
    ✅ Store Emergency Drinking Water: Keep at least 3 to 5 days' worth of clean drinking water stored in clean, covered containers (about 3 to 4 liters per person per day).
        Always boil or filter stored water before drinking to prevent waterborne diseases.

     ✅Cut Daily Water Waste: Turn off taps tightly while brushing teeth, shaving, or soaping hands.
        Take short bucket baths instead of long showers, and fix dripping taps or leaking pipes immediately.
        
     ✅Reuse Household Greywater: Collect water used for washing fruits, vegetables, rice, or clothes, and reuse it to water plants, flush toilets, or mop floors.
     
     ✅Stay Hydrated and Cool: Droughts often bring extreme heat and dry dust.
        Drink water regularly, avoid heavy outdoor work during peak afternoon sun, and keep a damp cloth handy to prevent heat exhaustion.
        
     ✅Follow Local Water Restrictions: Obey municipal water rationing rules, avoid washing cars or courtyards with running hoses,
         and water essential plants only in the early morning or late evening to reduce evaporation.
    """)

elif status == "Heatwave":
    st.warning("""
        ✅ Drink Water Often: Drink plenty of water throughout the day, even if you do not feel thirsty.
            Avoid tea, coffee, alcohol, and sugary drinks as they dehydrate your body.

        ✅ Stay Indoors During Peak Heat: Avoid going outside between 12:00 PM and 4:00 PM, when the sun is strongest. 
           Keep your windows and curtains closed during the day to block out hot air and sunlight.  

        ✅ Wear Light Clothes: Wear loose-fitting, lightweight, 
            and light-colored cotton clothes so your skin can breathe and sweat can evaporate easily.

        ✅ Keep Your Body Cool: Take cool showers, 
            wash your face with cold water frequently, 
            or place a damp cloth on your neck and forehead to lower your body temperature.  

         ✅ Protect Yourself When Going Out: If you must step outside, 
             cover your head with a cap, hat, scarf, or umbrella, wear sunglasses,
             and always carry a bottle of water with you.
    """)

elif status == "Typhoon":
    st.warning("""
        ✅ Prepare a 3-Day Emergency Go-Bag: Pack clean drinking water, non-perishable food,
            a first-aid kit, medicines, a flashlight with extra batteries,
            a fully charged power bank, and important documents in a waterproof bag.
            
        ✅Secure Your Home Early: Close and latch all doors and windows, bring loose outdoor items (like flower pots,
            furniture, and drying racks) inside so strong winds do not turn them into flying hazards, 
            and unplug non-essential electronics.
        
        ✅Stay Indoors Away from Windows: Move to an interior room, hallway, or lower floor away from glass windows and doors during the storm.
           Keep your shoes on and a mattress or sturdy table nearby for cover in case winds damage the roof.
           
        ✅Watch Out for the "Eye" of the Storm: Do not go outside if the wind and rain suddenly stop—this may only be the calm center of the typhoon, 
            and violent winds will return shortly from the opposite direction.
        ✅Avoid Floodwaters After the Storm: Never walk, swim, or drive through moving floodwater, and stay away from fallen power lines, broken glass,
            and damaged buildings until local authorities declare the area safe.
    """)

else:
    st.info("""
    ✅ Check Daily AQI Levels: Monitor the Air Quality Index (AQI) on your phone before stepping out.
        When AQI exceeds 200 (Poor/Unhealthy), limit outdoor exposure and avoid heavy outdoor exercise like running or cycling.

    ✅ Wear a Proper Mask Outdoors: Use a well-fitted N95 or KN95 mask when walking near traffic or dusty areas. 
        Cloth and surgical masks do not block fine particulate matter (PM2.5).

    ✅ Keep Indoor Air Clean: Close windows and doors during peak traffic hours and early mornings when smog settles near the ground.
        Run a HEPA air purifier in your bedroom or main living space, and avoid burning incense, candles, or mosquito coils indoors.

    ✅ Clean and Hydrate Your Airways: Wash your face, hands, and nasal passages after returning from outside to clear trapped dust.
        Drink plenty of water to keep your throat and respiratory tract moist.

    ✅ Eat Antioxidant-Rich Foods: Include vitamin C, vitamin E, and omega-3 foods—such as 
        citrus fruits, amla, turmeric, nuts, and leafy greens—to help your body fight inflammation caused by polluted air.  
    """)

    st.success(f"✅ Live Weather Data : {city}")

except Exception as e:
    st.error(f"Weather API Error: {e}")
