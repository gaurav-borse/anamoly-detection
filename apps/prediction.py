import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics import precision_recall_fscore_support

@st.cache_resource
def load_model():
    with open('D:/College Stuff/4th Year 1st Sem/Project/anamoly-detection-app/apps/datasets/UNSW/preprocessor.pkl', 'rb') as f:
        ct = pickle.load(f)
    with open('D:/College Stuff/4th Year 1st Sem/Project/anamoly-detection-app/apps/datasets/UNSW/rf_model.pkl', 'rb') as f:
        rf_classifier = pickle.load(f)
    with open('D:/College Stuff/4th Year 1st Sem/Project/anamoly-detection-app/apps/datasets/UNSW/test_data.pkl', 'rb') as f:
        X_test, y_test = pickle.load(f)
    return ct, rf_classifier, X_test, y_test

def app():
    st.markdown("Anamoly Detection | **Network Attack Category Prediction System**")
    st.title(":green[Attack] Prediction")
    st.markdown("**Predicting attacks** in IoT networks involves using various *machine learning and statistical techniques* to anticipate and prevent cybersecurity threats before they occur.")
    st.markdown("""<hr style="border: 2px solid rgb(61, 213, 109); margin-top: 8px;">""", unsafe_allow_html=True)

    st.markdown("**`Enter the features / Network Traffic details to predict the network attack category.`**")

    # Load the model and preprocessor
    ct, rf_classifier, X_test, y_test = load_model()

    # Define the input form
    with st.form(key='prediction_form'):
        proto = st.selectbox('Protocol', ['tcp', 'udp', 'http'])
        service = st.selectbox('Service', ['dhcp', 'dns', 'ftp', 'ftp-data', 'http', 'irc', 'pop3', 'radius', 'smtp', 'snmp', 'ssh', 'ssl'])
        state = st.selectbox('State', ['CON', 'FIN', 'INT', 'REQ', 'RST'])
        dur = st.number_input('Duration', min_value=0.0, value=1.5)
        spkts = st.number_input('Source Packets', min_value=0, value=20)
        dpkts = st.number_input('Destination Packets', min_value=0, value=10)
        sbytes = st.number_input('Source Bytes', min_value=0, value=1000)
        dbytes = st.number_input('Destination Bytes', min_value=0, value=2000)
        rate = st.number_input('Rate', min_value=0.0, value=50.0)
        sttl = st.number_input('Source TTL', min_value=0, value=60)
        dttl = st.number_input('Destination TTL', min_value=0, value=100)
        sload = st.number_input('Source Load', min_value=0.0, value=200.0)
        dload = st.number_input('Destination Load', min_value=0.0, value=0.5)
        sloss = st.number_input('Source Loss', min_value=0, value=0)
        dloss = st.number_input('Destination Loss', min_value=0, value=0)
        sinpkt = st.number_input('Source Interval', min_value=0.0, value=500.0)
        dinpkt = st.number_input('Destination Interval', min_value=0.0, value=1000.0)
        sjit = st.number_input('Source Jitter', min_value=0.0, value=5.0)
        djit = st.number_input('Destination Jitter', min_value=0.0, value=10.0)
        swin = st.number_input('Source Window', min_value=0, value=5)
        stcpb = st.number_input('Source TCP Base', min_value=0, value=10)
        dtcpb = st.number_input('Destination TCP Base', min_value=0, value=100)
        dwin = st.number_input('Destination Window', min_value=0, value=200)
        tcprtt = st.number_input('TCP RTT', min_value=0.0, value=500.0)
        synack = st.number_input('SYN ACK', min_value=0.0, value=1000.0)
        ackdat = st.number_input('ACK Data', min_value=0.0, value=1.0)
        smean = st.number_input('Source Mean', min_value=0, value=2)
        dmean = st.number_input('Destination Mean', min_value=0, value=3)
        trans_depth = st.number_input('Transaction Depth', min_value=0, value=4)
        response_body_len = st.number_input('Response Body Length', min_value=0, value=5)
        ct_srv_src = st.number_input('CT SRV SRC', min_value=0, value=0)
        ct_state_ttl = st.number_input('CT State TTL', min_value=0, value=1)
        ct_dst_ltm = st.number_input('CT DST LTM', min_value=0, value=1)
        ct_src_dport_ltm = st.number_input('CT SRC DPORT LTM', min_value=0, value=2)
        ct_dst_sport_ltm = st.number_input('CT DST SPORT LTM', min_value=0, value=3)
        ct_dst_src_ltm = st.number_input('CT DST SRC LTM', min_value=0, value=4)
        is_ftp_login = st.number_input('Is FTP Login', min_value=0, value=5)
        ct_ftp_cmd = st.number_input('CT FTP CMD', min_value=0, value=6)
        ct_flw_http_mthd = st.number_input('CT FLW HTTP MTHD', min_value=0, value=7)
        ct_src_ltm = st.number_input('CT SRC LTM', min_value=0, value=8)
        ct_srv_dst = st.number_input('CT SRV DST', min_value=0, value=9)
        is_sm_ips_ports = st.number_input('Is SM IPS Ports', min_value=0, value=0)
        
        submit_button = st.form_submit_button(label='Predict')

    # Function to predict attack category based on input features
    def predict_attack_category(input_features):
        # Ensure the input features match the expected order and length
        input_features_encoded = ct.transform([input_features])
        predicted_category = rf_classifier.predict(input_features_encoded)
        return predicted_category[0]

    # Prediction and display results
    if submit_button:
        # 42 
        input_features = [
            proto, service, state, dur, spkts, dpkts, sbytes, dbytes, rate, sttl, dttl, sload, dload, 
            sloss, dloss, sinpkt, dinpkt, sjit, djit, swin, stcpb, dtcpb, dwin, tcprtt, synack, ackdat, 
            smean, dmean, trans_depth, response_body_len, ct_srv_src, ct_state_ttl, ct_dst_ltm, 
            ct_src_dport_ltm, ct_dst_sport_ltm, ct_dst_src_ltm, is_ftp_login, ct_ftp_cmd, 
            ct_flw_http_mthd, ct_src_ltm, ct_srv_dst, is_sm_ips_ports
        ]
        predicted_category = predict_attack_category(input_features)
        st.write(f"Predicted Attack Category: {predicted_category}")

        # Calculate precision, recall, f1-score
        y_pred = rf_classifier.predict(X_test)
        precision, recall, f1_score, _ = precision_recall_fscore_support(y_test, y_pred, average='weighted')
        
        st.write("### Evaluation Metrics")
        st.write(f"**Precision:** {precision:.4f}")
        st.write(f"**Recall:** {recall:.4f}")
        st.write(f"**F1-Score:** {f1_score:.4f}")