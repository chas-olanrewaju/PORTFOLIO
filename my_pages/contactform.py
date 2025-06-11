import streamlit as st
import os

import streamlit as st
import os

# def display_contact_form(css_file="styles/main2.css", form_action_url="https://formsubmit.co/el/lawuxo"):
#     st.markdown("<h1 style='text-align:center; color:black; font-size:24px;'>Simple Streamlit Contact Form</h1>", unsafe_allow_html=True)

#     # HTML for the contact form
#     contactform = f"""
#     <form action="{form_action_url}" method="POST">
#         <input type="text" name="name" required placeholder="Your name">
#         <input type="email" name="email" required placeholder="Your email">
#         <textarea name="message" placeholder="Write your message"></textarea>
#         <button type="submit" class="button">Send</button>
#     </form>
#     """
#     st.markdown(contactform, unsafe_allow_html=True)

#     if os.path.exists(css_file):
#         with open(css_file) as f:
#             st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def display_contact_form(css_file="styles/main2.css", form_action_url="https://formsubmit.co/olanrewaju.charles2014@gmail.com"):
    st.markdown("<h1 style='text-align:center; color:black; font-size:24px;'>Simple Streamlit Contact Form</h1>", unsafe_allow_html=True)

    contactform = f"""
    <form action="{form_action_url}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_next" value="https://yourdomain.com/thank-you">  <!-- You can customize this -->
        <input type="text" name="name" required placeholder="Your name">
        <input type="email" name="email" required placeholder="Your email">
        <textarea name="message" placeholder="Write your message"></textarea>
        <button type="submit" class="button">Send</button>
    </form>
    """
    st.markdown(contactform, unsafe_allow_html=True)

    if os.path.exists(css_file):
        with open(css_file) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


