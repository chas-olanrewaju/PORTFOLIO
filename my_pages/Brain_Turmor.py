import streamlit as st

def show():
    
    # Title and header
    st.markdown("""
    <h3 style='text-align: center; font-size: 37px;'>
    🧠 Brain Tumor Classification with Deep Learning.
    </h3>
    """, unsafe_allow_html=True)

    st.markdown("#### A project combining CNNs and ensemble models for accurate brain scan diagnosis.")


    st.image("assets/brain tumor.jpg", use_container_width=True)


    # Project poster PDF
    st.markdown("#### 📌 Project Poster")
    with open("assets/D3002144_olanrewaju_charles_DL_Poster.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(label="📥 Download Poster",
                    data=PDFbyte,
                    file_name="Brain_Tumor_DL_Poster.pdf",
                    mime='application/octet-stream',
                    key="poster_download_button")

    # Overview
    st.markdown("""
    ---

    ### 📝 Project Overview
    This deep learning project focuses on classifying brain tumors using MRI scans. The work compares pre-trained CNNs (like **Xception**, **ResNet50**, **InceptionV3**) with a custom ensemble model to improve diagnostic accuracy in detecting tumors.

    ### 📊 Dataset
    - Source: [Kaggle Brain Tumor Dataset](https://www.kaggle.com/datasets/jakeshbohaju/brain-tumor)
    - 3,762 total MRI images
    - Binary classification: Tumor (`1`) or No Tumor (`0`)
    """)

    # Techniques
    st.markdown("""
    ### 🧪 Techniques Used
    - **Image Preprocessing**: Resize (224x224), normalization, denoising, CLAHE
    - **Models**: 
        - Pre-trained: Xception, ResNet50, InceptionV3
        - Custom CNN
        - Ensemble (majority voting)
    - **Hyperparameter Tuning**: Using **Keras Tuner**
    - **Deployment**: Built with **Streamlit** for interactive diagnosis

    ### 📈 Results
    | Model       | Accuracy | Precision | Recall | F1 Score | AUC |
    |-------------|----------|-----------|--------|----------|-----|
    | Xception    | 84%      | 83%       | 89%    | 86%      | 90% |
    | ResNet50    | 83%      | 88%       | 85%    | 88%      | —   |
    | InceptionV3 | 81%      | 80%       | 81%    | 80%      | 89% |
    | Custom CNN  | **92%**  | 92%       | 90%    | 91%      | —   |
    | Ensemble    | **93%**  | 90%       | 89%    | 90%      | —   |

    """)

    # Challenges & Ethics
    st.markdown("""
    ### ⚠️ Challenges & Considerations
    - **Data Variability**: Different MRI machines/protocols
    - **Class Imbalance**: Fewer tumor images than non-tumor
    - **Ethical Risks**: Privacy (HIPAA/GDPR), bias, patient trust
    - **Security**: Importance of encryption and access control

    ---

    ### 🔗 Code
    📘 [Kaggle Notebook](https://www.kaggle.com/code/martinnjihia/deep-learning-brain-06-04)
    """)
