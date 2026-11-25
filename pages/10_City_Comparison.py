import streamlit as st
import pandas as pd
import plotly.express as px
from assets.theme import apply_theme

# Theme

apply_theme()

# Title
st.title("🏙 Smart City Comparison")

# Data
df = pd.DataFrame({
    "City": [
        "Navsari",
        "Ahmedabad",
        "Mumbai",
        "Bombay"
    ],

    "Flood Risk": [
        25,
        40,
        75,
        75
    ],

    "AQI": [
        70,
        120,
        95,
        95
    ],

    "Population Growth": [
        18,
        35,
        45,
        45
    ]
})

# Table
st.dataframe(
    df,
    use_container_width=True
)

# Flood Risk Line Graph
fig1 = px.line(
    df,
    x="City",
    y="Flood Risk",
    title="🌊 Flood Risk Comparison",
    markers=True
)

fig1.update_traces(
    line=dict(
        color="#00E5FF",
        width=5
    ),
    marker=dict(
        size=12,
        color="#FFD700"
    )
)

fig1.update_layout(
    paper_bgcolor="#08101F",
    plot_bgcolor="#08101F",
    font=dict(color="#D4AF37"),
    title_font=dict(color="#D4AF37", size=24),
    height=500
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# AQI Line Graph

fig2 = px.line(
    df,
    x="City",
    y="AQI",
    title="🌫 AQI Comparison",
    markers=True
)

fig2.update_traces(
    line=dict(
        color="#7F5AF0",
        width=5
    ),
    marker=dict(
        size=12,
        color="#FFD700"
    )
)

fig2.update_layout(
    paper_bgcolor="#08101F",
    plot_bgcolor="#08101F",
    font=dict(color="#D4AF37"),
    title_font=dict(color="#D4AF37", size=24),
    height=500
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# Population Growth

fig3 = px.line(
    df,
    x="City",
    y="Population Growth",
    title="📈 Population Growth Comparison",
    markers=True
)

fig3.update_traces(
    line=dict(
        color="#00FF88",
        width=5
    ),
    marker=dict(
        size=12,
        color="#FFD700"
    )
)

fig3.update_layout(
    paper_bgcolor="#08101F",
    plot_bgcolor="#08101F",
    font=dict(color="#D4AF37"),
    title_font=dict(color="#D4AF37", size=24),
    height=500
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# Footer Card

st.success("""
📈 Comparative City Analytics

✅ Infrastructure Risk

✅ Population Growth

✅ Environmental Factors

✅ AI Future Score
""")
