
import streamlit as st

st.set_page_config(page_title="Portfolio", page_icon="📁")

# Sidebar Navigation
st.sidebar.title("Navigation")

# Main section to select About Me, Projects, or Contact
main_section = st.sidebar.radio("Go to", ["👤 About Me", "📁 Projects", "📜 Certifications", "📬 Contact"])

# Dynamically load the selected section
if main_section == "👤 About Me":
    # Import the About Me page only when it's selected
    import my_pages.About_me as About_me
    About_me.home()

elif main_section == "📁 Projects":
    # Dropdown for project selection
    projects_page = st.sidebar.selectbox(
        "Select Project",
        ["Brain Tumor", "Water Portability", "ALS Disease", "Bias Assessment", "Sentiment Analysis"]
    )

    # Dynamically load the selected project
    if projects_page == "Brain Tumor":
        # Import the Brain Tumor project page only when selected
        import my_pages.Brain_Turmor as Brain_Turmor
        Brain_Turmor.show()
    elif projects_page == "Water Portability":
        # Import the Water Portability project page only when selected
        import my_pages.Water_Portability as Water_Portability
        Water_Portability.show()

    elif projects_page == "ALS Disease":
        # Import the ALS Disease project page only when selected
        import my_pages.ALS_Disease as ALS_Disease
        ALS_Disease.show()

    elif projects_page == "Bias Assessment":
        # Import the ALS Disease project page only when selected
        import my_pages.Bias_project as Bias_project
        Bias_project.show()

    elif projects_page == "Sentiment Analysis":
        # Import the ALS Disease project page only when selected
        import my_pages.Sentiment_Analysis as Sentiment_Analysis
        Sentiment_Analysis.show()

elif main_section == "📜 Certifications":
    # Import the Contact form page only when it's selected
    import my_pages.Certifications as Certifications
    Certifications.show()


elif main_section == "📬 Contact":
    # Import the Contact form page only when it's selected
    import my_pages.contactform as contactform
    contactform.display_contact_form()




