import streamlit as st

def app():
    st.markdown("Anamoly Detection | **About Us**")
    st.title("About the :green[Anomaly Detection] App")
    st.markdown("**Who We Are** - Find Out About Our Team and Vision.")

    st.markdown("""<hr style="border: 2px solid rgb(61, 213, 109); margin-top: 8px;">""", unsafe_allow_html=True)

    st.markdown("""
    ## Project Overview
    In today's connected world, IoT (Internet of Things) networks are increasingly becoming targets for cyber-attacks. 
    This project aims to develop a machine learning model to predict and identify potential attacks in IoT networks, 
    thus helping to secure these networks from malicious activities.

    ## Functionality
    This application provides the following key functionalities:

    ### 1. Dataset Display
    - The application displays two primary datasets: `KDDTrain+.txt` and `KDDTest+.txt`. 
    - These datasets are used to train and test the anomaly detection model.
    - You can view the structure and content of these datasets on the Dataset Display page.

    ### 2. Anomaly Detection
    - Users can input various features of network traffic to predict whether the traffic is normal or an attack.
    - The model classifies attacks into different categories such as DOS, Probe, U2R, and Sybil.

    ### 3. Model Evaluation
    - The application provides metrics such as accuracy, precision, and recall to evaluate the performance of the model.
    - Users can see how well the model performs in distinguishing between normal and malicious network traffic.

    ### 4. Visualization
    - The project includes various visualizations to help understand the data and the model's performance.
    - These visualizations include confusion matrices and other relevant charts.

    ## Vision
    Our vision is to create a robust and efficient system for detecting anomalies in IoT networks, ensuring the security and integrity of connected devices. By leveraging machine learning, we aim to provide a tool that can help in early detection and prevention of cyber-attacks, thus safeguarding sensitive information and maintaining the smooth operation of IoT systems.

    ## Team
    - **Gaurav Borse**
    - **Shubham Thorat**
    - **Urmila Narvade**
    - **Vaishnavi Pratale**

    ## Technical Details
    - **Programming Language**: Python
    - **Framework**: Streamlit for the frontend, scikit-learn for machine learning
    - **Datasets**: `KDDTrain+.txt` and `KDDTest+.txt`, which are standard datasets used for network intrusion detection.

    ## Contact Us
    If you have any questions or suggestions, please contact us at [gborse108@gmail.com].

    For more details, visit our [GitHub repository](https://github.com/).
    """)