import streamlit as st
import plotly.graph_objects as go
from assets.theme import apply_theme

apply_theme()

st.title("🌫 Air Quality Intelligence")

aqi = st.slider(
    "AQI",
    0,
    500,
    120
)

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=aqi,
    title={'text': "Air Quality Index", 'font': {'color': '#F8FAFC', 'size': 24}}, # <--- નવો ઉમેરો (ટાઈટલ કલર)
    number={'font': {'color': '#FFFFFF', 'size': 50}}, # <--- નવો ઉમેરો (વચ્ચેના નંબરનો કલર)
    gauge={
        'axis': {
            'range': (0, 500),
            'tickcolor': '#FFFFFF',  # <--- નવો ઉમેરો (નાની લીટીનો કલર)
            'tickfont': {'color': '#FFFFFF', 'size': 14} # <--- નવો ઉમેરો (0 થી 500 નંબરનો કલર)
        },
        'bar': {'color': '#38BDF8'}, # <--- નવો ઉમેરો (મીટરના કાંટાનો કલર)
        'bgcolor': "#0F172A", # <--- નવો ઉમેરો (મીટરની અંદરનો કલર)
        'steps': (
            {'range': (0, 50), 'color': 'green'},
            {'range': (51, 100), 'color': 'yellow'},
            {'range': (101, 200), 'color': 'orange'},
            {'range': (201, 500), 'color': 'red'}
        )
    }
))

# <--- નવો ઉમેરો (બોક્સનો બેકગ્રાઉન્ડ કલર બદલવા માટે)
fig.update_layout(
    paper_bgcolor="#1E293B",
    font={'color': "#FFFFFF"}
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("### 🛡️ Personal Action Plan (What You Should Do)")

if aqi <= 50:
    st.success("🟢 Good Air Quality")
    st.info("""
    * **Outdoor Activities:** Safe for walking, running, and outdoor workouts.
    * **Home Environment:** Keep windows open for natural ventilation and fresh air.
    * **Protection:** No mask or special precautions needed.
    """)

elif aqi <= 100:
    st.warning("🟡 Moderate Air Quality")
    st.info("""
    * **Outdoor Activities:** Generally safe, but avoid heavy outdoor exercise for long hours.
    * **Sensitive Groups:** If you have asthma or breathing issues, limit prolonged outdoor exertion.
    * **Protection:** Wear a basic mask in dusty or high-traffic areas.
    """)

elif aqi <= 200:
    st.error("🟠 Poor / Unhealthy Air Quality")
    st.warning("""
    * **Wear a Mask:** Always wear an **N95 mask** when stepping outside.
    * **Exercise Indoors:** Avoid outdoor running or sports; switch to indoor workouts.
    * **Indoor Safety:** Keep doors and windows closed to prevent polluted air from entering.
    * **Health Care:** Stay well-hydrated and wash your eyes with clean water if irritation occurs.
    """)

else:
    st.error("🔴 Very Poor / Severe Air Quality")
    st.error("""
    * **Stay Indoors:** Avoid going outside unless it is an emergency.
    * **Air Purification:** Run an indoor air purifier and keep all windows tightly shut.
    * **Mandatory Protection:** Wear a certified **N95 or N99 mask** if you must go out.
    * **Medical Attention:** Consult a doctor immediately if you experience coughing, throat irritation, or shortness of breath.
    """)
