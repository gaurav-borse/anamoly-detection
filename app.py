import streamlit as st
from multiapp import MultiApp
from apps import home, about, prediction_new, data, contact

app = MultiApp()

st.set_page_config(
    page_title="Anamoly Detection Using ML",
    page_icon="📊",
    layout="wide"
)

def creds_entered():
    if st.session_state['user'].strip() == "admin" and st.session_state['passwd'].strip() == "admin":
        st.session_state["authenticated"] = True
    else:
        st.session_state["authenticated"] = False
        if not st.session_state['passwd']:
            st.warning("Password field is required!")
        elif not st.session_state['user']:
            st.warning("Username field is required!")
        else:
            st.error("Invalid Username/Password :face_with_raised_eyebrow:")

def authenticate_user():
    if "authenticated" not in st.session_state:
        st.markdown("""
            ##### Hello User! 🖐️
            # Login to :green[Anamoly Detection] App
            [**Anomaly detection**] refers to the process of *identifying patterns* in data that do not conform to expected behavior.
        """)
        st.text_input(label="Username :", value="", key="user", on_change=creds_entered)
        st.text_input(label="Password :", value="", key="passwd", type="password", on_change=creds_entered)
        return False
    else:
        if st.session_state["authenticated"]:
            return True
        else:
            st.markdown("""
            ##### Hello User! 🖐️
            # Login to :green[Anamoly Detection] App
            This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
            """)
            st.text_input(label="Username :", value="", key="user", on_change=creds_entered)
            st.text_input(label="Password :", value="", key="passwd", type="password", on_change=creds_entered)
            return False

if authenticate_user():
    app.add_app("Home", home.app)
    app.add_app("About", about.app)
    app.add_app("Prediction", prediction_new.app)
    app.add_app("Dataset", data.app)
    app.add_app("Contact", contact.app)
    app.run()
