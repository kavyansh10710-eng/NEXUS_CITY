import streamlit as st

import streamlit as st

def apply_theme():

    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

def apply_theme():
    st.markdown("""
    <style>

    /* Main Text */
    html, body, [class*="css"] {
        color: #FFD700 !important;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #FFD700 !important;
        font-weight: 700;
    }

    /* Paragraphs */
    p {
        color: #FFD700 !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] * {
        color: #FFD700 !important;
    }

    /* Metrics */
    div[data-testid="metric-container"] {
        color: #FFD700 !important;
    }

    div[data-testid="metric-container"] label,
    div[data-testid="metric-container"] div {
        color: #FFD700 !important;
    }

    /* Tabs */
    button[data-baseweb="tab"] {
        color: #FFD700 !important;
    }

    /* Selectbox */
    .stSelectbox label {
        color: #FFD700 !important;
    }

    /* Radio */
    .stRadio label {
        color: #FFD700 !important;
    }

    /* Checkbox */
    .stCheckbox label {
        color: #FFD700 !important;
    }

    /* Expander */
    .streamlit-expanderHeader {
        color: #FFD700 !important;
    }

    /* Dataframe Header */
    .dataframe th {
        color: #FFD700 !important;
    }

    /* Success Info Warning */
    .stAlert {
        color: #FFD700 !important;
    }

    /* Links */
    a {
        color: #FFD700 !important;
    }

    </style>
    """, unsafe_allow_html=True)
