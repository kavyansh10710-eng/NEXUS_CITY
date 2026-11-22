import streamlit as st

def show_logo():
    st.markdown("""
    <h1 style='text-align:center;color:#00D4FF;font-size:70px;'>
        
    NEXUS ∞ City
    </h1>
    st.image(
    "assets/favicon.png",
    width=250
)
    <h3 style='text-align:center;color:#FFD700;'>
    Smart City AI Platform
    </h3>
   """, unsafe_allow_html=True) 
