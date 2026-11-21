from logo import show_logo
import streamlit as st

def render_header():

    show_logo()

    st.markdown("""
    <div style="
    text-align:center;
    color:#FFD700;
    font-size:22px;
    font-weight:bold;
    margin-bottom:25px;
    ">

    Smart City AI Digital Twin Platform

    </div>
    """,
    unsafe_allow_html=True)
