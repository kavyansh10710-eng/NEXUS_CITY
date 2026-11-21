import streamlit as st
import plotly.graph_objects as go

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
    title={'text':"Air Quality Index"},
    gauge={
        'axis':{'range':[0,500]},
        'steps':[
            {'range':[0,50],'color':'green'},
            {'range':[51,100],'color':'yellow'},
            {'range':[101,200],'color':'orange'},
            {'range':[201,500],'color':'red'}
        ]
    }
))

st.plotly_chart(
    fig,
    use_container_width=True
)

if aqi <= 50:
    st.success("Good Air Quality")
elif aqi <=100:
    st.warning("Moderate Air Quality")
else:
    st.error("Poor Air Quality")
