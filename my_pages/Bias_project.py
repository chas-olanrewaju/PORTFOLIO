import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def fairness_radar_chart():
    fairness_df = pd.DataFrame({
        'Metric': ['EO', 'DP', 'EA'],
        'Value': [0.0476, 0.1623, 0.0185]
    })

    fig = px.line_polar(fairness_df, r='Value', theta='Metric', line_close=True,
                        title='Fairness Metrics Radar Plot', range_r=[0, 0.2])
    fig.update_traces(fill='toself', line_color='indianred')
    return fig

def plot_metric_comparison():
    metrics = ["Accuracy", "Precision", "Recall", "F1 Score"]
    male_scores = [0.92, 0.88, 0.95, 0.92]
    female_scores = [0.94, 0.91, 1.00, 0.95]

    fig = go.Figure(data=[
        go.Bar(name='Male', x=metrics, y=male_scores, marker_color='steelblue'),
        go.Bar(name='Female', x=metrics, y=female_scores, marker_color='mediumvioletred')
    ])

    fig.update_layout(
        title='Performance Metrics by Gender',
        yaxis=dict(title='Score', range=[0, 1.1]),
        barmode='group'
    )

    return fig



def show():
    # Title and header
    st.markdown("""
    <h3 style='text-align: center; font-size: 31px;'>
    ❤️ Gender Bias Assessment in AI-Based Heart Health Prediction Models
    </h3>
    """, unsafe_allow_html=True)

    st.markdown("#### Investigating fairness across gender groups in machine learning models for heart disease risk prediction.")

    st.image("assets/bia.png", use_container_width=True) 

    # Overview
    st.markdown("""
    ---

    ### 📝 Project Overview
    This project critically explores the **existence of gender bias** in AI-based diagnostic models for **heart disease prediction**, using a real-world dataset and fairness evaluation criteria.

    A Support Vector Machine (SVM) classifier was trained and analyzed to assess fairness metrics like **Equality of Opportunity**, **Demographic Parity**, and **Equal Accuracy** across **male** and **female** patient groups.

    ### 🎯 Objective
    To **evaluate the fairness and diagnostic reliability** of heart disease prediction models across genders and recommend mitigations for bias in AI-powered healthcare.
    """)

    
    

    # Dataset
    st.markdown("""
    ---
    ### 🧫 Dataset
    - **Source**: [Kaggle Heart Disease Dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)
    - 1025 samples | 14 features
    - Includes demographic, clinical, and test-related attributes

    📌 Key target: 0 = No heart disease, 1 = Heart disease
    """)

    

    # Preprocessing and Exploration
    st.markdown("""
    ---
    ### 🔍 Preprocessing and Exploration
    - Null values and duplicates checked (none found)
    - Z-score normalization applied via `StandardScaler`
    - 80/20 train-test split (random_state=5)
    - Data visualization: histograms, heatmaps for correlation

    Features included:
    - Age, Sex, Chest pain type, Blood pressure, Cholesterol, etc.
    """)

    st.image("assets/bias_flowchart.png", caption="Fig. 1: Flowchart for Data Exploration and Preprocessing", use_container_width=True)



    # Model
    st.markdown("""
    ---
    ### 🤖 Model
    - **Support Vector Machine (SVM)**
    - Chosen for its ability to handle non-linear boundaries and high-dimensional data
    - Performance assessed before and after gender group separation
    """)

    # Evaluation Metrics
    st.markdown("""
    ---
    ### 📊 Evaluation Metrics
    - Accuracy
    - Precision
    - Recall (Sensitivity)
    - F1 Score
    """)

    # Fairness Metrics Explanation
    st.markdown("""
    ### ⚖️ Fairness Metrics Used
    - **Equality of Opportunity (EO)**: Difference in sensitivity (TPR) between genders
    - **Demographic Parity (DP)**: Difference in predicted positive rates
    - **Equal Accuracy (EA)**: Difference in prediction accuracy

    > Goal: Ensure model fairness and avoid gender-based diagnostic disparities.
    """)


    # Embed interactive visuals
    st.markdown("""
    ---
    ### 📊 Performance Metric Comparison""")
    st.plotly_chart(plot_metric_comparison(), use_container_width=True)

    st.markdown("### ⚖️ Fairness Radar Chart")
    st.plotly_chart(fairness_radar_chart(), use_container_width=True)


    # Results
    st.markdown("""
    
    ### 🚀 Key Results
    - **Female Group**: Accuracy = 94%, F1-score = 0.95, Recall = 100%
    - **Male Group**: Accuracy = 92%, F1-score = 0.92, Recall = 95%
    - **Fairness Evaluation**:
      - **Equality of Opportunity (EO)** = 0.0476
      - **Demographic Parity (DP)** = 0.1623
      - **Equal Accuracy (EA)** = 0.0185

    📌 Insight: Slight bias in favor of females, indicating overdiagnosis risk for females and underdiagnosis for males.
    """)


    # System Info
    st.markdown("""
    ---
    ### 💻 System Specs
    - **Python 3**
    - **Scikit-learn**
    - **Jupyter Notebook**
    - Runtime: Local system (CPU)
    """)

    # Module Info
    st.markdown("""
    ### 🙌 Module Info
    - Module: **Artificial Intelligence Ethics and Applications – CIS4057-N**
    - Module Instructor: Prof. Olugbenga

    ### 🧠 Author
    **Charles Olanrewaju**

    
    ### 🔗 Code
    📘 [Kaggle Notebook](https://www.kaggle.com/code/olanrewajucharles/aiea-ica-final)
              
    ---
    ### 📚 Citation
    ```
    Olanrewaju, C. (2024). Gender Bias Assessment in AI-Based Heart Health Prediction Models. Coursework submission for CIS4057-N, Teesside University.
    ```
    """)
