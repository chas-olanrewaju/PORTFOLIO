import streamlit as st



def show():
    
    # Title and header
    st.markdown("""
    <h3 style='text-align: center; font-size: 35px;'>
    💧 Water Potability Prediction with Traditional Machine Learning.
    </h3>
    """, unsafe_allow_html=True)

    st.markdown("#### A project applying classical ML models to predict drinking water safety using physicochemical features.")

    st.image("assets/water_image.jpeg", use_container_width=True)  # Replace with your actual image path


    # Overview
    st.markdown("""
    ---

    ### 📝 Project Overview
    This project explores the use of traditional machine learning algorithms to classify water as potable or non-potable based on 10 physicochemical properties. It leverages a dataset sourced from Kaggle and compares the effectiveness of six models, including Logistic Regression, SVM, Random Forest, Decision Trees, KNN, and XGBoost.

    ### 📊 Dataset
    - Source: [Kaggle Water Potability Dataset](https://www.kaggle.com/datasets/adityakadiwal/water-potability)
    - 3,276 water samples
    - 10 features: pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic Carbon, Trihalomethanes, Turbidity, Potability
    - Binary classification: Potable (`1`) vs Non-potable (`0`)
    """)

    # Research Methodology Flowchart
    st.markdown("### 🔬 Research Methodology Flowchart")
    st.image("assets/water_research_methodology.jpg", caption="Fig. 1: Research Methodology Flowchart", use_container_width=True)


    # Methodology
    st.markdown("""
    ### 🧪 Techniques Used
    - **Preprocessing**: Outlier removal, mean imputation, Z-score normalization
    - **Feature Selection**: SelectKBest (all features eventually retained)
    - **Algorithms**:
        - Logistic Regression
        - Support Vector Machines
        - Random Forest
        - Decision Tree
        - K-Nearest Neighbour
        - XGBoost
    - **Optimization**: GridSearchCV for hyperparameter tuning
    - **Evaluation**: Accuracy, Precision, Recall, F1 Score, AUC, Confusion Matrix, ROC curves

    ### 📈 Results (After Hyperparameter Tuning)
    | Model              | Accuracy | Precision | Recall | F1 Score |
    |--------------------|----------|-----------|--------|----------|
    | Logistic Regression| 65%      | 100%      | 1%     | 0.02     |
    | SVM                | 71%      | 75%       | 28%    | 0.41     |
    | Decision Tree      | 67%      | 58%       | 22%    | 0.31     |
    | Random Forest      | **72%**  | 68%       | 37%    | **0.48** |
    | XGBoost            | 68%      | 57%       | 36%    | 0.44     |
    | KNN                | 69%      | 62%       | 29%    | 0.39     |
    """)

    # Challenges & Ethics
    st.markdown("""
    ### ⚠️ Challenges & Considerations
    - **Class Imbalance**: Potable water samples were underrepresented
    - **Oversampling with SMOTE**: Led to reduced performance due to potential noise
    - **Model Bias**: Some models struggled with low recall
    - **Ethics**: Emphasized data privacy, fairness, transparency, responsible AI use, and compliance with legal frameworks (GDPR, etc.)

    ---

    ### 🔗 External Resources
    📘 [Kaggle Code Notebook](https://www.kaggle.com/code/olanrewajucharles/ml-ica-water3)
    """)
