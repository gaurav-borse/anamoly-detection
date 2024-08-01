import streamlit as st
import pandas as pd

def app():
    st.markdown("Anomaly Detection | **Dataset Display**")
    st.title(":green[Dataset] Display")
    st.markdown("**Predicting attacks** in IoT networks involves using various *machine learning and statistical techniques* to anticipate and prevent cybersecurity threats before they occur.")

    file_path_full_training_set = 'D:/College Stuff/4th Year 1st Sem/Project/anamoly-detection-app/apps/datasets/KDDTrain+.txt'
    file_path_test = 'D:/College Stuff/4th Year 1st Sem/Project/anamoly-detection-app/apps/datasets/KDDTest+.txt'


    columns = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment',
               'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted',
               'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login',
               'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
               'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
               'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
               'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
               'dst_host_srv_rerror_rate', 'attack', 'level']

    df_train = pd.read_csv(file_path_full_training_set, header=None, names=columns)
    df_test = pd.read_csv(file_path_test, header=None, names=columns)

    st.subheader("Training Dataset")
    st.write("The following is the DataFrame of the `KDDTrain+` dataset.")
    st.write(df_train)

    st.subheader("Test Dataset")
    st.write("The following is the DataFrame of the `KDDTest+` dataset.")
    st.write(df_test)