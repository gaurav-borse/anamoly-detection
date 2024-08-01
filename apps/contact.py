import streamlit as st

from email_validator import validate_email, EmailNotValidError
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from io import BytesIO
from streamlit_js_eval import streamlit_js_eval

def app():
    st.markdown("Anamoly Detection | **Contact Us**")
    st.title(":green[Contact] Us")
    st.markdown("**Let's Connect!** Reach Us for Any Inquiries or Assistance")

    email = st.text_input("**Your email***", value=st.session_state.get('email', ''), key='email')
    message = st.text_area("**Your message***", value=st.session_state.get('message', ''), key='message')

    st.markdown('<p style="font-size: 13px;">*Required fields</p>', unsafe_allow_html=True)

    if st.button("Send", type="primary"):
        if email and message:
            st.success("Your message has been sent successfully!")
        elif not email or not message:
            st.error("Please fill out all required fields.")
        else:
            try:
                valid = validate_email(email, check_deliverability=True)
            except EmailNotValidError as e:
                st.error(f"Invalid email address. {e}")