import streamlit as st

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
