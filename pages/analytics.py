import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("📈 Data Analytics")

days = np.arange(1,31)

rain = np.random.randint(40,120,30)
temp = np.random.randint(25,45,30)

df = pd.DataFrame({
    "Day":days,
    "Rainfall":rain,
    "Temperature":temp
})

fig = px.line(
    df,
    x="Day",
    y="Rainfall",
    title="Rainfall Analysis"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
