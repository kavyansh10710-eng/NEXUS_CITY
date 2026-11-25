import streamlit as st
import base64


def apply_theme():

    # Background Image
    with open("assets/background.png", "rb") as image_file:
        encoded = base64.b64encode(
            image_file.read()
        ).decode()

    # Load CSS
    with open("assets/style.css", "r", encoding="utf-8") as f:
        css = f.read()

    st.markdown(
        f"""
        <style>

        {css}

        .stApp {{
            background:
            linear-gradient(
                rgba(5,8,22,0.65),
                rgba(5,8,22,0.65)
            ),
            url("data:image/png;base64,{encoded}");

            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        h1,h2,h3,h4,h5,h6 {{
            color:#D4AF37 !important;
        }}

        p,label,span {{
            color:white !important;
        }}

        [data-testid="stSidebar"] {{
            background: rgba(0,0,0,0.45);
            backdrop-filter: blur(15px);
        }}

        [data-testid="stSidebar"] * {{
            color:#D4AF37 !important;
        }}

        div[data-testid="metric-container"] {{
            background: rgba(0,0,0,0.30);
            border: 1px solid rgba(212,175,55,0.3);
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }}

        </style>
        """,
        unsafe_allow_html=True
    )
