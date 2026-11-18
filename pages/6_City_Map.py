import streamlit as st
import pydeck as pdk
import pandas as pd

st.set_page_config(layout="wide")

st.title("🛰️ Smart City Satellite Map")

# City Selection
city = st.selectbox(
    "🏙️ Select City",
    [
        "Navsari (Gujarat)",
        "Ahmedabad (Gujarat)",
        "Mumbai (Maharashtra)",
        "Bombay (Maharashtra)"
    ]
)

# Coordinates

cities = {
    "Navsari (Gujarat)": {
        "lat": 20.9467,
        "lon": 72.9520,
        "color": [0,255,0]
    },

    "Ahmedabad (Gujarat)": {
        "lat": 23.0225,
        "lon": 72.5714,
        "color": [255,165,0]
    },

    "Mumbai (Maharashtra)": {
        "lat": 19.0760,
        "lon": 72.8777,
        "color": [255,0,0]
    },

    "Bombay (Maharashtra)": {
        "lat": 19.0760,
        "lon": 72.8777,
        "color": [255,0,0]
    }
}

selected = cities[city]

# DataFrame

df = pd.DataFrame(
    {
        "lat":[selected["lat"]],
        "lon":[selected["lon"]]
    }
)

# Satellite Map

view_state = pdk.ViewState(
    latitude=selected["lat"],
    longitude=selected["lon"],
    zoom=11,
    pitch=55
)

layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position='[lon, lat]',
    get_fill_color=selected["color"],
    get_radius=3000,
)

st.pydeck_chart(
    pdk.Deck(
        map_style="mapbox://styles/mapbox/satellite-v9",
        initial_view_state=view_state,
        layers=[layer]
    )
)

st.success(f"Selected City : {city}")

st.markdown("---")

col1,col2,col3 = st.columns(3)

with col1:
    st.metric("🌧 Flood Risk","34%")

with col2:
    st.metric("🔥 Heatwave Risk","61%")

with col3:
    st.metric("💨 Air Quality","Moderate")
