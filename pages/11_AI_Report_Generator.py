import streamlit as st
import pandas as pd

st.title("📑 AI Report Generator")

city = st.selectbox(
    "Select City",
    [
        "Navsari",
        "Ahmedabad",
        "Mumbai",
        "Bombay"
    ]
)

if st.button("Generate Report"):

    report = pd.DataFrame({

        "Parameter":[
            "Flood Risk",
            "AQI",
            "Temperature",
            "Status"
        ],

        "Value":[
            "40%",
            "85",
            "31°C",
            "Moderate"
        ]
    })

    st.dataframe(
        report,
        use_container_width=True
    )

    csv = report.to_csv(index=False)

    st.download_button(
        label="⬇ Download Report",
        data=csv,
        file_name=f"{city}_report.csv",
        mime="text/csv"
    )
