import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
import matplotlib.pyplot as plt
from io import BytesIO
from datetime import datetime
from assets.theme import apply_theme

apply_theme()

st.title("📄 NEXUS AI PDF Report Generator")

city = st.selectbox(
    "🏙 Select City",
    [
        "Navsari",
        "Ahmedabad",
        "Mumbai",
        "Surat"
    ]
)

flood_risk = st.slider("🌊 Flood Risk (%)", 0, 100, 40)
aqi = st.slider("🌫 AQI", 0, 500, 95)
temperature = st.slider("🌡 Temperature (°C)", 0, 50, 32)

# Calculate Overall Risk Score (0 to 100)
aqi_score = min((aqi / 500) * 100, 100)
temp_score = min((temperature / 50) * 100, 100)
overall_risk_score = int((flood_risk * 0.5) + (aqi_score * 0.3) + (temp_score * 0.2))

st.metric(label="⚠ Overall Risk Score", value=f"{overall_risk_score} / 100")

# Function to generate a colorful bar chart
def create_risk_chart(flood, aqi_norm, temp_norm, overall):
    fig, ax = plt.subplots(figsize=(6, 2.8))
    
    categories = ['Flood Risk', 'AQI Level', 'Temperature', 'Overall Score']
    values = [flood, aqi_norm, temp_norm, overall]
    bar_colors = ['#3498db', '#9b59b6', '#e67e22', '#e74c3c' if overall >= 70 else ('#f1c40f' if overall >= 40 else '#2ecc71')]
    
    bars = ax.bar(categories, values, color=bar_colors, width=0.5)
    ax.set_ylim(0, 115)
    ax.set_ylabel('Risk Index (0-100)', fontsize=9, fontweight='bold')
    ax.set_title('City Environmental Risk Breakdown', fontsize=11, fontweight='bold', color='#1a252f')
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    # Remove top and right borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Add value labels on top of bars
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 3, f"{int(yval)}%", ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    chart_buffer = BytesIO()
    plt.savefig(chart_buffer, format='png', dpi=150)
    plt.close(fig)
    chart_buffer.seek(0)
    return chart_buffer

if st.button("📄 Generate PDF Report"):

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # --- 1. Top Colored Header Banner ---
    pdf.setFillColor(colors.HexColor("#1E3A8A")) # Deep Navy Blue
    pdf.rect(0, height - 100, width, 100, fill=1, stroke=0)

    pdf.setFillColor(colors.white)
    pdf.setFont("Helvetica-Bold", 22)
    pdf.drawString(40, height - 45, "NEXUS AI Future Simulator")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(40, height - 70, "Smart City Risk Assessment & Action Report")
    
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawRightString(width - 40, height - 70, f"Date: {datetime.now().strftime('%d-%m-%Y')}")

    # --- 2. City & Score Summary Box ---
    pdf.setFillColor(colors.HexColor("#F1F5F9")) # Light Slate Gray background
    pdf.roundRect(40, height - 210, width - 80, 90, 8, fill=1, stroke=0)

    pdf.setFillColor(colors.HexColor("#0F172A"))
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(60, height - 145, f"Target City: {city.upper()}")

    pdf.setFont("Helvetica", 11)
    pdf.drawString(60, height - 170, f"Flood Risk: {flood_risk}%   |   AQI: {aqi}   |   Temperature: {temperature} °C")

    # Dynamic Status & Color Badge
    if overall_risk_score >= 70:
        status = "HIGH RISK"
        badge_color = colors.HexColor("#DC2626") # Red
        city_recommendation = (
            "• Expand Water Reservoirs & Deploy Emergency Teams immediately.\n"
            "• Activate City-wide Flood & Heat Warning Systems."
        )
        person_action = (
            "• Stay indoors and avoid all unnecessary travel.\n"
            "• Keep an emergency kit (flashlight, medicines, dry food, water) ready.\n"
            "• Wear an N95 mask if stepping outside due to hazardous air quality.\n"
            "• Keep your phone charged and follow local government alerts."
        )
    elif overall_risk_score >= 40:
        status = "MEDIUM RISK"
        badge_color = colors.HexColor("#D97706") # Amber/Orange
        city_recommendation = (
            "• Monitor water levels and drainage systems closely.\n"
            "• Issue public health advisories for heat and air quality."
        )
        person_action = (
            "• Check weather updates before planning outdoor activities.\n"
            "• Stay hydrated and avoid direct afternoon sunlight.\n"
            "• Use a mask if you have breathing issues or allergies.\n"
            "• Keep important documents in waterproof covers."
        )
    else:
        status = "LOW RISK"
        badge_color = colors.HexColor("#16A34A") # Green
        city_recommendation = (
            "• Current environmental conditions are stable.\n"
            "• Continue routine smart-city monitoring."
        )
        person_action = (
            "• Normal daily activities are completely safe.\n"
            "• Conserve water and electricity to keep the city sustainable.\n"
            "• Use public transport or carpool to maintain good air quality."
        )

    # Draw Risk Score & Colored Status Pill
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(60, height - 195, f"Overall Risk Score: {overall_risk_score} / 100")

    pdf.setFillColor(badge_color)
    pdf.roundRect(width - 180, height - 198, 120, 22, 5, fill=1, stroke=0)
    pdf.setFillColor(colors.white)
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawCentredString(width - 120, height - 191, status)

    # --- 3. Insert Colorful Chart ---
    chart_buf = create_risk_chart(flood_risk, aqi_score, temp_score, overall_risk_score)
    chart_img = ImageReader(chart_buf)
    pdf.drawImage(chart_img, 65, height - 450, width=460, height=215)

    # --- 4. AI Recommendations Section ---
    # City Action Box
    pdf.setFillColor(colors.HexColor("#EFF6FF")) # Soft Blue Tint
    pdf.roundRect(40, height - 565, width - 80, 95, 8, fill=1, stroke=0)
    
    pdf.setFillColor(colors.HexColor("#1E40AF"))
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(55, height - 490, "🏛 Government / City Action Plan:")

    pdf.setFillColor(colors.HexColor("#1E293B"))
    pdf.setFont("Helvetica", 10.5)
    text_city = pdf.beginText(55, height - 510)
    text_city.setLeading(15)
    text_city.textLines(city_recommendation)
    pdf.drawText(text_city)

    # One Single Person Action Box
    pdf.setFillColor(colors.HexColor("#FEF2F2") if overall_risk_score >= 70 else colors.HexColor("#F0FDF4"))
    pdf.roundRect(40, height - 705, width - 80, 125, 8, fill=1, stroke=0)

    pdf.setFillColor(badge_color)
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(55, height - 600, "👤 What One Single Person Should Do:")

    pdf.setFillColor(colors.HexColor("#1E293B"))
    pdf.setFont("Helvetica", 10.5)
    text_person = pdf.beginText(55, height - 620)
    text_person.setLeading(15)
    text_person.textLines(person_action)
    pdf.drawText(text_person)

    # --- 5. Footer ---
    pdf.setFillColor(colors.HexColor("#1E3A8A"))
    pdf.rect(0, 0, width, 40, fill=1, stroke=0)
    pdf.setFillColor(colors.white)
    pdf.setFont("Helvetica", 9)
    pdf.drawCentredString(width / 2, 16, "Generated by NEXUS Smart City AI Platform  |  AI-Powered Urban Risk Intelligence")

    pdf.save()
    pdf_data = buffer.getvalue()

    st.success("✅ Colorful PDF Report with Chart Generated Successfully!")

    st.download_button(
        label="⬇ Download PDF Report",
        data=pdf_data,
        file_name=f"{city}_NEXUS_Report.pdf",
        mime="application/pdf"
    )
