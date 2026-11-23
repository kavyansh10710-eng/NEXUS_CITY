import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="NEXUS ∞ City Map", layout="wide")

st.title("🗺️ NEXUS ∞ India Smart City Map")

# Major Indian Cities Dataset
cities = [
    ["Ahmedabad", 23.0225, 72.5714],
    ["Surat", 21.1702, 72.8311],
    ["Vadodara", 22.3072, 73.1812],
    ["Rajkot", 22.3039, 70.8022],
    ["Mumbai", 19.0760, 72.8777],
    ["Pune", 18.5204, 73.8567],
    ["Nagpur", 21.1458, 79.0882],
    ["Delhi", 28.6139, 77.2090],
    ["Noida", 28.5355, 77.3910],
    ["Gurugram", 28.4595, 77.0266],
    ["Bengaluru", 12.9716, 77.5946],
    ["Mysuru", 12.2958, 76.6394],
    ["Chennai", 13.0827, 80.2707],
    ["Coimbatore", 11.0168, 76.9558],
    ["Hyderabad", 17.3850, 78.4867],
    ["Visakhapatnam", 17.6868, 83.2185],
    ["Kolkata", 22.5726, 88.3639],
    ["Bhubaneswar", 20.2961, 85.8245],
    ["Jaipur", 26.9124, 75.7873],
    ["Lucknow", 26.8467, 80.9462],
    ["Kanpur", 26.4499, 80.3319],
    ["Chandigarh", 30.7333, 76.7794],
    ["Bhopal", 23.2599, 77.4126],
    ["Indore", 22.7196, 75.8577],
    ["Patna", 25.5941, 85.1376],
    ["Ranchi", 23.3441, 85.3096],
    ["Kochi", 9.9312, 76.2673],
    ["Thiruvananthapuram", 8.5241, 76.9366],
    ["Srinagar", 34.0837, 74.7973],
    ["Guwahati", 26.1445, 91.7362]
]

df = pd.DataFrame(cities, columns=["City", "Latitude", "Longitude"])

# Search City
selected_city = st.selectbox(
    "🔍 Search City",
    options=["All Cities"] + df["City"].tolist()
)

# Create Map
if selected_city == "All Cities":
    map_center = [22.5937, 78.9629]
    zoom = 5
else:
    row = df[df["City"] == selected_city].iloc[0]
    map_center = [row["Latitude"], row["Longitude"]]
    zoom = 10

m = folium.Map(
    location=map_center,
    zoom_start=zoom,
    tiles="CartoDB Positron"
)

# Add Markers
for _, row in df.iterrows():

    popup_html = f"""
    <div style='width:200px'>
        <h4>🏙️ {row['City']}</h4>
        <hr>
        📍 Latitude: {row['Latitude']}<br>
        📍 Longitude: {row['Longitude']}<br><br>

        🤖 NEXUS AI Status:<br>
        ✅ Active Monitoring
    </div>
    """

    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=folium.Popup(popup_html, max_width=250),
        tooltip=row["City"],
        icon=folium.Icon(
            color="blue",
            icon="info-sign"
        )
    ).add_to(m)

# Display Map
st_folium(
    m,
    width=None,
    height=700
)

st.success(f"✅ Monitoring {len(df)} Major Indian Cities")
