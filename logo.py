import streamlit as st

def show_logo():

    st.markdown("""
    <div style="
        text-align:center;
        padding:20px;
        margin-bottom:20px;
    ">

        <h1 style="
            color:#00D4FF;
            font-size:80px;
            font-weight:900;
            margin-bottom:5px;
            text-shadow:
                0 0 15px #00D4FF,
                0 0 30px #00D4FF,
                0 0 60px #00D4FF;
        ">
            🌍 NEXUS ∞
        </h1>

        <h3 style="
            color:#FFC300;
            font-size:36px;
            font-weight:900;
            text-shadow:
                0 0 10px #FFD700,
                0 0 20px #FFD700,
                0 0 40px #FFD700;
        ">
            Smart City AI Digital Twin Platform
        </h3>

        <p style="
            color:white;
            font-size:20px;
            font-weight:600;
        ">
            Detect • Predict • Decide
        </p>

    </div>
    """, unsafe_allow_html=True)
