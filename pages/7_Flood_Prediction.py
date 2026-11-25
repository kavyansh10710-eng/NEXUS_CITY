import streamlit as st
import pandas as pd
import plotly.express as px

from assets.theme import apply_theme

apply_theme()

# ========================================
# TITLE
# ========================================

st.title("🌊 NEXUS ∞ Flood Intelligence Center")

st.markdown("""
Monitor rainfall, river levels and soil moisture
to predict flood risks using AI-powered analytics.
""")

# ========================================
# INPUTS
# ========================================

col1, col2, col3 = st.columns(3)

with col1:
    rainfall = st.slider(
        "🌧️ Rainfall (mm)",
        0,
        500,
        200
    )

with col2:
    river_level = st.slider(
        "🌊 River Level (%)",
        0,
        100,
        50
    )

with col3:
    soil_moisture = st.slider(
        "💧 Soil Moisture (%)",
        0,
        100,
        60
    )

# ========================================
# RISK CALCULATION
# ========================================

risk = (
    rainfall * 0.15 +
    river_level * 0.40 +
    soil_moisture * 0.45
)

risk = min(round(risk), 100)

# ========================================
# RISK METER
# ========================================

st.metric(
    label="🚨 Flood Risk Score",
    value=f"{risk}%"
)

st.progress(risk)

# ========================================
# RISK ALERT
# ========================================

if risk > 70:

    st.markdown(
        f"""
        <div style="
        background:rgba(255,0,0,0.15);
        border:2px solid #ff4d4d;
        padding:20px;
        border-radius:16px;
        backdrop-filter:blur(12px);
        text-align:center;
        ">
            <h2 style="color:#ff4d4d;">
            🚨 HIGH FLOOD RISK
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )

elif risk > 40:

    st.markdown(
        f"""
        <div style="
        background:rgba(255,165,0,0.15);
        border:2px solid #ffb347;
        padding:20px;
        border-radius:16px;
        backdrop-filter:blur(12px);
        text-align:center;
        ">
            <h2 style="color:#ffb347;">
            ⚠️ MEDIUM FLOOD RISK
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown(
        f"""
        <div style="
        background:rgba(0,255,127,0.15);
        border:2px solid #00ff99;
        padding:20px;
        border-radius:16px;
        backdrop-filter:blur(12px);
        text-align:center;
        ">
            <h2 style="color:#00ff99;">
            ✅ LOW FLOOD RISK
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )

# ========================================
# CHART DATA
# ========================================

df = pd.DataFrame({
    "Factor": [
        "Rainfall",
        "River Level",
        "Soil Moisture"
    ],
    "Value": [
        rainfall,
        river_level,
        soil_moisture
    ]
})

# ========================================
# MODERN CHART
# ========================================

fig = px.bar(
    df,
    x="Factor",
    y="Value",
    color="Factor",
    text="Value",
    color_discrete_map={
        "Rainfall": "#00E5FF",
        "River Level": "#8A2BE2",
        "Soil Moisture": "#FFD700"
    }
)

fig.update_traces(
    textposition="outside",
    marker_line_width=0
)

fig.update_layout(

    title="📊 Flood Prediction Analytics",

    template="plotly_dark",

    paper_bgcolor="rgba(0,0,0,0.2)",

    plot_bgcolor="rgba(0,0,0,0.15)",

    font=dict(
        color="white",
        size=14
    ),

    title_font=dict(
        color="#00E5FF",
        size=24
    ),

    xaxis=dict(
        title="",
        showgrid=False
    ),

    yaxis=dict(
        title="Value",
        gridcolor="rgba(255,255,255,0.08)"
    ),

    legend_title="Factor",

    height=550
)

st.plotly_chart(
    fig,
    use_container_width=True
)
