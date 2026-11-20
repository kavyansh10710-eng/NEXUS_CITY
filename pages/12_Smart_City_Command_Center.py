
import streamlit as st
st.error(
"🔴 NEXUS COMMAND CENTER ACTIVE"
)
st.title("🖥 City Command Center")
st.success(
"🛰 542 Sensors Online"
)

st.success(
"⚡ Power Grid Connected"
)

st.success(
"☁ Weather Monitoring Active"
)
col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "🌊 Flood Alert",
    "Medium"
)

col2.metric(
    "🌫 AQI Status",
    "Moderate"
)

col3.metric(
    "⚡ Power Demand",
    "84%"
)

col4.metric(
    "🚨 Emergency Level",
    "Low"
)

st.divider()

st.subheader("AI Decision Center")

status = st.selectbox(
    "Select Situation",
    [
        "Flood",
        "Heatwave",
        "Air Pollution"
    ]
)

if status == "Flood":

    st.error("""
✅ Activate Emergency Pumps

✅ Open Water Channels

✅ Public Alert System

✅ Evacuation Ready
""")

elif status == "Heatwave":

    st.warning("""
✅ Open Cooling Centers

✅ Water Distribution

✅ Public Health Advisory
""")

else:

    st.info("""
✅ Reduce Traffic Pollution

✅ Monitor Factories

✅ Air Quality Surveillance
""")
