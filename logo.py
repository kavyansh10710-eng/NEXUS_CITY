import streamlit as st

def show_logo():

    st.markdown("""
    <style>

    @keyframes glow {
        0% {
            box-shadow: 0 0 20px #00D4FF;
        }
        50% {
            box-shadow:
            0 0 40px #00D4FF,
            0 0 80px #7C3AED,
            0 0 120px #FFD700;
        }
        100% {
            box-shadow: 0 0 20px #00D4FF;
        }
    }

    @keyframes textGlow {
        0% {
            text-shadow: 0 0 10px #00D4FF;
        }

        50% {
            text-shadow:
            0 0 20px #00D4FF,
            0 0 40px #7C3AED,
            0 0 60px #FFD700;
        }

        100% {
            text-shadow: 0 0 10px #00D4FF;
        }
    }

    @keyframes floatLogo {
        0% {
            transform: translateY(0px);
        }

        50% {
            transform: translateY(-8px);
        }

        100% {
            transform: translateY(0px);
        }
    }

    .nexus-logo {

        background:
        linear-gradient(
        135deg,
        #050816,
        #081B29,
        #112240
        );

        border:2px solid #00D4FF;

        border-radius:30px;

        padding:35px;

        text-align:center;

        animation:
        glow 4s infinite ease-in-out,
        floatLogo 5s infinite ease-in-out;

        margin-bottom:25px;
    }

    .nexus-title{

        font-size:72px;

        font-weight:900;

        color:white;

        animation:
        textGlow 3s infinite;

        margin-bottom:5px;
    }

    .nexus-sub{

        font-size:24px;

        color:#FFD700;

        font-weight:bold;
    }

    .nexus-desc{

        font-size:18px;

        color:white;

        margin-top:10px;
    }

    </style>

    <div class="nexus-logo">

        <div class="nexus-title">
        ⚛️ NEXUS ∞
        </div>

        <div class="nexus-sub">
        Smart City AI Digital Twin Platform
        </div>

        <div class="nexus-desc">
        Detect • Predict • Decide
        </div>

    </div>

    """, unsafe_allow_html=True)
