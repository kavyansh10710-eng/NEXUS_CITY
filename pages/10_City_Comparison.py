import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏙 Smart City Comparison")

df = pd.DataFrame({

    "City":[
        "Navsari",
        "Ahmedabad",
        "Mumbai",
        "Bombay"
    ],

    "Flood Risk":[
        25,
        40,
        75,
        75
    ],

    "AQI":[
        70,
        120,
        95,
        95
    ],

    "Population Growth":[
        18,
        35,
        45,
        45
    ]
})

st.dataframe(
    df,
    use_container_width=True
)

fig = px.bar(
    df,
    x="City",
    y="Flood Risk",
    color="City"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.success(
"""
📈 Comparative Smart City Analytics

✓ Infrastructure Risk

✓ Population Growth

✓ Environmental Factors

✓ AI Future Score
"""
)
