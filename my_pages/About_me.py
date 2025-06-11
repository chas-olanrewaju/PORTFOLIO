import streamlit as st
import base64



def home():
    

    # CSS styles file
    with open("styles/main.css") as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Profile image file
    with open("assets/PIC.jpg", "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

    # PDF CV file
    with open("assets/CV.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    
    # Top title
    st.write(f"""<div class="title"><strong>Hi! My name is</strong> Charles Olanrewaju👋</div>""", unsafe_allow_html=True)

    # Profile image
    st.write(f"""
    <div class="container">
        <div class="box">
            <div class="spin-container">
                <div class="shape">
                    <div class="bd">
                        <img src="{img}" alt="Enric Domingo">
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, 
    unsafe_allow_html=True)

    # Alternative image (static and rounded) uncomment it if you prefer this one
    # st.write(f"""
    # <div style="display: flex; justify-content: center;">
    #    <img src="{img}" alt="Enric Domingo" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
    # </div>
    # """, unsafe_allow_html=True)

    # Subtitle
    st.write(f"""<div class="subtitle" style="text-align: center;">Machine Learning and Software Engineer</div>""", unsafe_allow_html=True)

    # Social Icons
    social_icons_data = {
        # Platform: [URL, Icon]
        "Kaggle": ["https://www.kaggle.com/olanrewajucharles", "https://www.kaggle.com/static/images/site-logo.svg"],
        "LinkedIn": ["https://www.linkedin.com/in/charles-olanrewaju-b63533356/", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/chasolanrewaju", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
        "YouTube": ["https://www.youtube.com/@olanrewajucharles2353", "https://cdn-icons-png.flaticon.com/512/1384/1384060.png"],
        "Medium": ["https://medium.com/@olanrewaju.charles2014", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Medium_logo_Monogram.svg/1200px-Medium_logo_Monogram.svg.png"],
        "Padlet": ["https://padlet.com/olanrewajucharles2014", "https://upload.wikimedia.org/wikipedia/commons/0/0e/Padlet_Logo_No_stroke.png"]
    }

    social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]

    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", 
    unsafe_allow_html=True)

    st.write("##")

    # About me section
    st.subheader("About Me")
    st.markdown("""
    - 👨‍💻 I am a highly motivated individual passionate about harnessing artificial intelligence and data analytics to develop sustainable and impactful solutions.  
    With strong analytical, numerical, and creative skills, I aim to tackle diverse challenges through machine learning.  
    I thrive in collaborative environments and am dedicated to applying my expertise to create socially responsible and innovative outcomes.

    - 🚀 Applied AI & Machine Learning | Civil Engineering & Data Science

    - 🎓 Completed a Master’s degree in Applied Artificial Intelligence at Teesside University (2023–2025) and a Bachelor’s degree in Civil Engineering at Obafemi Awolowo University (2010–2016).

    - 📍 Based in Middlesbrough, United Kingdom
    """)


    st.write("##")


    # with open("assets/CV.pdf", "rb") as file:
    #     st.download_button(
    #         label="📄 Download my CV",
    #         data=file,
    #         file_name="CV.pdf",
    #         mime="application/pdf",
    #     )


    # with open("assets/D3002144_olanrewaju_charles_DL_Poster.pdf", "rb") as pdf_file:
    #     PDFbyte = pdf_file.read()
    # st.download_button(label="📥 Download Poster",
    #                 data=PDFbyte,
    #                 file_name="Brain_Tumor_DL_Poster.pdf",
    #                 mime='application/octet-stream',)


    st.write("##")
    
    st.write(f"""<div class="subtitle" style="text-align: center;">⬅️ Check out my Projects in the navigation menu! </div>""", unsafe_allow_html=True)


home()