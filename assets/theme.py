import streamlit as st

import streamlit as st
import base64

def apply_theme():

    with open("assets/background.png", "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    st.markdown(f"""
    <style>

    .stApp {{

        background:
        linear-gradient(
            rgba(5,8,22,0.82),
            rgba(5,8,22,0.82)
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
        color:#D4AF37 !important;
    }}

    </style>
    """, unsafe_allow_html=True)
def apply_theme():

    # Load CSS file
    with open("assets/style.css", "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

    # Golden Text
    st.markdown("""
    <style>

    h1,h2,h3,h4,h5,h6{
        color:#D4AF37 !important;
    }

    p,span,label{
        color:#D4AF37 !important;
    }

    [data-testid="stSidebar"] *{
        color:#D4AF37 !important;
    }

    div[data-testid="metric-container"] *{
        color:#D4AF37 !important;
    }

    button[data-baseweb="tab"]{
        color:#D4AF37 !important;
    }

    </style>
    """, unsafe_allow_html=True)
