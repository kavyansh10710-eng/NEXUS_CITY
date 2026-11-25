import streamlit as st
from assets.theme import apply_theme

apply_theme()

st.title("🎮 Future Scenario Simulator")

rainfall = st.slider(
    "Rainfall Change %",
    -50,
    100,
    20
)

temperature = st.slider(
    "Temperature Change",
    -10,
    10,
    2
)

population = st.slider(
    "Population Growth %",
    0,
    100,
    15
)

if st.button("🚀 Run Simulation"):

    score = (
        rainfall*0.3
        + temperature*2
        + population*0.4
    )

    st.success(
        f"Future Risk Score : {round(score,2)}%"
    )
