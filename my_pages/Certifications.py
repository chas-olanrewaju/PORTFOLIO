import streamlit as st

def show():
    st.markdown("""
    <h3 style='text-align: center;'>📜 Certifications</h3>
    """, unsafe_allow_html=True)

    st.markdown("#### Here's a curated list of my certifications and professional credentials:")

    certifications = {
        "☁️ AI-900: Microsoft Azure AI Fundamentals": "2025",
        "🧠 TensorFlow–Keras Boot Camp by OpenCV": "2024",
        "📘 Machine Learning Specialization by Coursera": "2024",
        "🐍 Python for Beginners": "2023",
        "📊 Data Visualization with Matplotlib Boot Camp (DPhi)": "2022",
        "🛠️ COREN Registered (Council for the Regulation of Engineering in Nigeria)": "2020",
        "🧯 Health, Safety and Environment (HSE) Level 1 & 2": "2014",
    }

    for cert, year in certifications.items():
        st.markdown(f"- **{cert}** – *{year}*")

    st.markdown("---")