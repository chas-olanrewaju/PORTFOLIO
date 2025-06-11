import streamlit as st

def show():
    st.markdown("<h3 style='text-align: center;'>📜 Sentiment Analysis Projects</h3>", unsafe_allow_html=True)
    st.markdown("#### Here's a list of sentiment analysis projects I have carried out:")

    projects = [
        {
            "title": "🧠 Sentiment Analysis on X (Formerly Twitter): What the Public Thinks About Global Leaders",
            "github": "https://github.com/chas-olanrewaju/twitter-sentiment-analysis",
            "medium": "https://medium.com/@olanrewaju.charles2014/sentiment-analysis-on-x-formerly-twitter-what-the-public-thinks-about-global-leaders-a1036b9627b9"
        }
    ]

    for project in projects:
        st.markdown(f"""
        - **{project['title']}**  
          [🔗 GitHub](<{project['github']}>) | [📝 Medium](<{project['medium']}>)  
        """)

    st.markdown("---")