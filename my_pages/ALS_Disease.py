import streamlit as st

def show():
    # Title and header
    st.markdown("""
    <h3 style='text-align: center; font-size: 31px;'>
    🧬 ALS Disease Stage Classification using Multimodal Deep Learning
    </h3>
    """, unsafe_allow_html=True)

    st.markdown("#### Exploring how spatial transcriptomics and histology images can jointly predict ALS progression stages.")

    st.image("assets/als images.jpeg", use_container_width=True)  # Replace with your actual banner/image


    # Overview
    st.markdown("""
    ---

    ### 📝 Project Overview
    This project investigates model architectures and modalities for classifying **Amyotrophic Lateral Sclerosis (ALS)** disease stages — p30, p70, p100, and p120 — using **spatial transcriptomics**, **histopathology images**, and **spatial coordinates**.

    Models explored include traditional MLPs, transformers, hybrid CNN-MLP, and graph neural network fusions.

    ### 🎯 Objective
    To develop and compare single- and multi-modal models that accurately classify ALS stages, leveraging spatial, visual, and molecular signals from high-dimensional biomedical data.
    """)

    # Dataset
    st.markdown("""
    ### 🧫 Dataset
    - **Gene expression matrix** (Spatial transcriptomics)
    - **H&E-stained histopathology images**
    - **Spatial location metadata (spot-level coordinates)**
    
    📁 Dataset sourced from: [Spacell GitHub](https://github.com/BiomedicalMachineLearning/Spacell/tree/master/dataset)
    """)

    # Models
    st.markdown("""
    ### 🧪 Models Implemented
    - **MLP (Gene Expression)**
    - **Vision Transformer (Histology Images)**
    - **Hybrid CNN–MLP (Images + Gene)**
    - **GNN–CNN–MLP (Spots + Images + Gene)**

    These architectures were implemented and benchmarked using modular Jupyter notebooks with TensorFlow, Spektral, and custom preprocessing pipelines.
    """)

    st.markdown("### 🔬 Model Architectures Diagram")
    st.image("assets/ViT.png", caption="Fig. 1: Model Architectures Diagram for Vision Transformer", use_container_width=True)
    st.image("assets/modalities.png", caption="Fig. 2: Model Architectures Diagram for Multimodal Models", use_container_width=True)


    # Performance Metrics
    st.markdown("""
    ### 📊 Evaluation Metrics
    - Accuracy
    - Sensitivity / Specificity
    - Precision / F1 Score
    - AUC
    - Cohen’s Kappa
    - MAE / RMSE / RAE / RRSE
    """)

    # Results
    st.markdown("""
    ### 🚀 Key Results
    - **Hybrid GNN–CNN–MLP** achieved **97% accuracy**
    - High agreement with expert annotations (Cohen’s Kappa)
    - Strong AUC and F1 across all ALS stages
    - Multimodal approaches significantly outperformed single modalities
    """)

    # Workflow
    st.markdown("""
    ### 🧰 Implementation Pipeline
    1. `Data_preparation`
    2. `Image_normalization_new`
    3. `Prepare_multimodal_dataset`
    4. `CNN_MLP Model`
    5. `MLP Model`
    6. `Vision Transformer Model`
    7. `GNN-CNN-MLP Model`
    """)

    # System Info
    st.markdown("""
    ### 💻 System Specs
    - **Python 3.10.16**
    - **TensorFlow 2.14.1**, **Spektral**, **Scikit-learn**
    - **CPU**: AMD Ryzen 9 7945HX  
    - **GPU**: NVIDIA GeForce RTX 4070
    """)

    # Ethics and Acknowledgement
    st.markdown("""
    ### 🙌 Acknowledgements
    Supervisor: **Prof. Claudio Angione**, Teesside University

    ### 🧠 Author
    **Charles Olanrewaju**
                
    ### 🔗 Code
    📘 [GitHub Repository](https://github.com/chas-olanrewaju/ALS-Disease)


    ---

    ### 📚 Citation
    ```
    Olanrewaju, C., & Angione, C. (2025). Exploring Model Architectures and Modalities for Disease Stage Classification in Amyotrophic Lateral Sclerosis Using Spatial Transcriptomics and Histology Imaging. [Unpublished MSc thesis]. Teesside University.
    ```
    """)
