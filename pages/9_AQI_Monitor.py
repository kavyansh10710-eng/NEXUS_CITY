import streamlit as st
import plotly.graph_objects as go
from assets.theme import apply_theme

apply_theme()

st.title("🌫 Air Quality Intelligence")

aqi = st.slider(
    "AQI",
    0,
    500,
    120
)

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=aqi,
    title={'text': "Air Quality Index", 'font': {'color': '#FFFFFF', 'size': 24}}, # ટાઈટલનો કલર
    number={'font': {'color': '#BAE6FD'}}, # વચ્ચે દેખાતા AQI નંબરનો કલર
    gauge={
        'axis': {'range': (0, 500), 'tickcolor': '#BAE6FD'},
        'bar': {'color': '#FDE047'}, # વચ્ચેના મુખ્ય કાંટા/બારનો કલર
        'bgcolor': "white", # મીટરની અંદરના ખાલી ભાગનો કલર
        'borderwidth': 2,
        'bordercolor': "#90CAF9", # બોર્ડરનો કલર
        'steps': (
            {'range': (0, 50), 'color': '#4CAF50'},    # Green
            {'range': (51, 100), 'color': '#FFEB3B'},  # Yellow
            {'range': (101, 200), 'color': '#FF9800'}, # Orange
            {'range': (201, 500), 'color': '#F44336'}  # Red
        )
    }
))

# આ ભાગ ચાર્ટના કાળા બોક્સનો કલર બદલશે
fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",  # ચાર્ટના મુખ્ય બોક્સનો બેકગ્રાઉન્ડ કલર
    font={'color': "#0D47A1"} # ચાર્ટના બધા અક્ષરોનો કલર
)

st.plotly_chart(
    fig,
    use_container_width=True
)
