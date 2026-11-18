import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌊 Flood Prediction Center")

rainfall = st.slider(
    "Rainfall (mm)",
    0,
    500,
    200
)

river_level = st.slider(
    "River Level (%)",
    0,
    100,
    50
)

soil_moisture = st.slider(
    "Soil Moisture (%)",
    0,
    100,
    60
)

risk = (
    rainfall*0.15 +
    river_level*0.4 +
    soil_moisture*0.45
)

risk = min(round(risk),100)

st.metric(
    "Flood Risk",
    f"{risk}%"
)

if risk > 70:
    st.error("🔴 High Flood Risk")
elif risk > 40:
    st.warning("🟠 Medium Flood Risk")
else:
    st.success("🟢 Low Flood Risk")

df = pd.DataFrame({
    "Factor":["Rainfall","River Level","Soil Moisture"],
    "Value":[rainfall,river_level,soil_moisture]
})

fig = px.bar(
    df,
    x="Factor",
    y="Value",
    color="Factor"
)

st.plotly_chart(fig,use_container_width=True)
