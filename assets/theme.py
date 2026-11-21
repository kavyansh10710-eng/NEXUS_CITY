import streamlit as st

def apply_theme():

    theme = st.sidebar.selectbox(
        "🎨 Select Theme",
        [
            "Cyberpunk",
            "Golden"
        ]
    )

    if theme == "Cyberpunk":

        st.markdown("""
        <style>

        .stApp{
            background:#081B29;
            color:white;
        }

        h1,h2,h3{
            color:#00D4FF;
        }

        [data-testid="metric-container"]{
            background:#112240;
            border:1px solid #00D4FF;
            border-radius:15px;
            padding:10px;
        }

        </style>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <style>

        .stApp{
            background:#0D1117;
            color:white;
        }

        h1,h2,h3{
            color:#FFD700;
        }

        [data-testid="metric-container"]{
            background:#1A1A1A;
            border:1px solid #FFD700;
            border-radius:15px;
            padding:10px;
        }

        </style>
        """, unsafe_allow_html=True)
