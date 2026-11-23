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
            "temp": round(temp, 1),
            "humidity": humidity,
            "wind": round(wind, 1),
            "weather": condition,
            "rainfall": rainfall,
            "aqi": aqi
        }

    except Exception as e:

        print("Weather API Error:", e)

        return None
