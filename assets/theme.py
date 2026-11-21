import streamlit as st

def apply_theme():
    st.markdown("""
    <style>

    .stApp{
        background:#081B29;
        color:white;
    }

    h1,h2,h3{
        color:#00D4FF;
    }

    </style>
    """, unsafe_allow_html=True)
