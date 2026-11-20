import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="NEXUS AI Future Simulator",
    page_icon="🌍",
    layout="wide"
)
st.subheader("🚀 Smart City Command Center")
# -------------------------
# Header
# -------------------------
st.markdown("""
<h1 style='text-align:center;color:#00D4FF;'>
🌍 NEXUS ∞ AI Future Simulator
</h1>
<h4 style='text-align:center;'>
Detect → Predict → Decide
</h4>
""", unsafe_allow_html=True)

st.divider()

# -------------------------
# Sidebar Controls
# -------------------------
st.sidebar.title("⚙️ What-If Controls")

rainfall = st.sidebar.slider("🌧 Rainfall Change (%)", -50, 50, 0)
temperature = st.sidebar.slider("🌡 Temperature Change (°C)", -10, 10, 0)
population = st.sidebar.slider("👥 Population Growth (%)", -50, 100, 20)
electricity = st.sidebar.slider("⚡ Electricity Demand (%)", -50, 100, 10)

# -------------------------
# Current Status
# -------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("🌡 Temperature", "34°C", f"{temperature:+}°C")
col2.metric("💧 Water Level", "68%", f"{rainfall:+}%")
col3.metric("🌫 Air Quality", "Good")
col4.metric("⚡ Energy Demand", "Normal", f"{electricity:+}%")

st.divider()

# -------------------------
# Data Analysis Section
# -------------------------
st.subheader("📊 Future Risk Analytics")

# Sample Data
days = np.arange(1, 31)

rain_data = np.random.randint(40, 120, 30)
temp_data = np.random.randint(25, 45, 30)

col1, col2 = st.columns(2)

with col1:
    fig = px.line(
        x=days,
        y=rain_data,
        labels={"x": "Days", "y": "Rainfall"},
        title="Rainfall Trend"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.line(
        x=days,
        y=temp_data,
        labels={"x": "Days", "y": "Temperature"},
        title="Temperature Trend"
    )
    st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Risk Calculation
# -------------------------
risk_score = 50

risk_score += temperature * 2
risk_score += rainfall * 0.8
risk_score += population * 0.5
risk_score += electricity * 0.7

risk_score = max(0, min(100, risk_score))

# -------------------------
# Risk Section
# -------------------------
st.subheader("🚨 AI Risk Assessment")

if risk_score < 40:
    level = "🟢 LOW"
elif risk_score < 70:
    level = "🟠 MEDIUM"
else:
    level = "🔴 HIGH"

col1, col2 = st.columns([1, 2])

with col1:
    st.metric("Risk Score", f"{risk_score:.0f}/100")
    st.success(level)

with col2:

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_score,
        title={'text': "Future Risk Meter"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "red"},
            'steps': [
                {'range': [0, 40], 'color': "green"},
                {'range': [40, 70], 'color': "orange"},
                {'range': [70, 100], 'color': "red"},
            ]
        }
    ))

    st.plotly_chart(gauge, use_container_width=True)

# -------------------------
# AI Recommendation
# -------------------------
st.subheader("🤖 AI Recommendation")

if risk_score >= 70:
    st.error("""
    • Increase Water Storage Capacity

    • Implement Heatwave Emergency Plan

    • Reduce Energy Consumption

    • Improve Air Quality Monitoring
    """)
elif risk_score >= 40:
    st.warning("""
    • Monitor Temperature Trends

    • Optimize Water Distribution

    • Prepare Future Scenarios
    """)
else:
    st.success("""
    • Current Situation Stable

    • Continue Monitoring

    • Maintain Sustainability Measures
    """)

# -------------------------
# Simulation Results
# -------------------------
st.subheader("📈 Simulation Results")

results = pd.DataFrame({
    "Scenario": ["Current", "+20% Rainfall", "+40% Rainfall"],
    "Risk": ["Medium", "High", "Very High"],
    "Water Level": ["68%", "82%", "95%"],
    "Air Quality": ["Good", "Moderate", "Poor"]
})

st.dataframe(results, use_container_width=True)

st.divider()

st.markdown("""
<center>
<h4>🚀 NEXUS AI Future Simulator</h4>
Predict the Possible. Choose the Best.
</center>
""", unsafe_allow_html=True)
