import streamlit as st

theme = st.sidebar.selectbox(
    "🎨 Select Theme",
    [
        "Cyberpunk",
        "Golden",
        "Light",
        "Midnight"
    ]
)

if theme == "Cyberpunk":
    from themes.cyberpunk import load_theme

elif theme == "Golden":
    from themes.golden import load_theme

load_theme()
