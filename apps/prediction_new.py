import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

file_path_full_training_set = 'D:/College Stuff/4th Year 1st Sem/Project/anamoly-detection-app/apps/datasets/KDDTrain+.txt'
file_path_test = 'D:/College Stuff/4th Year 1st Sem/Project/anamoly-detection-app/apps/datasets/KDDTest+.txt'

df = pd.read_csv(file_path_full_training_set)
test_df = pd.read_csv(file_path_test)

columns = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment',
           'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted',
           'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login',
           'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
           'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
           'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
           'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
           'dst_host_srv_rerror_rate', 'attack', 'level']

df.columns = columns
test_df.columns = columns

dos_attacks = ['apache2', 'back', 'land', 'neptune', 'mailbomb', 'pod', 'processtable', 'smurf', 'teardrop',
               'udpstorm', 'worm']
probe_attacks = ['ipsweep', 'mscan', 'nmap', 'portsweep', 'saint', 'satan']
U2R = ['buffer_overflow', 'loadmdoule', 'perl', 'ps', 'rootkit', 'sqlattack', 'xterm']
Sybil = ['ftp_write', 'guess_passwd', 'http_tunnel', 'imap', 'multihop', 'named', 'phf', 'sendmail', 'snmpgetattack',
         'snmpguess', 'spy', 'warezclient', 'warezmaster', 'xclock', 'xsnoop']

def map_attack(attack):
    if attack in dos_attacks:
        return 1
    elif attack in probe_attacks:
        return 2
    elif attack in U2R:
        return 3
    elif attack in Sybil:
        return 4
    else:
        return 0

df['attack_map'] = df['attack'].apply(map_attack)
test_df['attack_map'] = test_df['attack'].apply(map_attack)

features_to_encode = ['protocol_type', 'service', 'flag']
encoded = pd.get_dummies(df[features_to_encode])
test_encoded_base = pd.get_dummies(test_df[features_to_encode])

test_index = np.arange(len(test_df.index))
column_diffs = list(set(encoded.columns.values) - set(test_encoded_base.columns.values))
diff_df = pd.DataFrame(0, index=test_index, columns=column_diffs)
column_order = encoded.columns.to_list()
test_encoded_temp = test_encoded_base.join(diff_df)
test_final = test_encoded_temp[column_order].fillna(0)

numeric_features = ['duration', 'src_bytes', 'dst_bytes']
to_fit = encoded.join(df[numeric_features])
test_set = test_final.join(test_df[numeric_features])

binary_y = df['attack_map']
multi_y = df['attack_map']

test_binary_y = test_df['attack_map']
test_multi_y = test_df['attack_map']

binary_train_X, binary_val_X, binary_train_y, binary_val_y = train_test_split(to_fit, binary_y, test_size=0.6)
multi_train_X, multi_val_X, multi_train_y, multi_val_y = train_test_split(to_fit, multi_y, test_size=0.6)

binary_model = RandomForestClassifier()
binary_model.fit(binary_train_X, binary_train_y)
binary_predictions = binary_model.predict(binary_val_X)

def detect_attack(input_data):
    input_df = pd.DataFrame([input_data])

    input_encoded = pd.get_dummies(input_df[features_to_encode])

    missing_cols = set(encoded.columns) - set(input_encoded.columns)
    for col in missing_cols:
        input_encoded[col] = 0

    input_encoded = input_encoded[column_order].fillna(0)

    input_final = input_encoded.join(input_df[numeric_features])

    prediction = binary_model.predict(input_final)

    return prediction[0]

def app():
    st.markdown("Anamoly Detection | **Network Attack Prediction System**")
    st.title(":green[Attack] Prediction")
    st.markdown("**Predicting attacks** in IoT networks involves using various *machine learning and statistical techniques* to anticipate and prevent cybersecurity threats before they occur.")
    st.markdown("""<hr style="border: 2px solid rgb(61, 213, 109); margin-top: 8px;">""", unsafe_allow_html=True)

    st.markdown("**`Enter the features / Network Traffic details to predict the network attack.`**")

    input_data = {}
    columns_per_row = 3
    input_fields = columns[:-2]

    for i in range(0, len(input_fields), columns_per_row):
        cols = st.columns(columns_per_row)
        for col_index, col_name in enumerate(input_fields[i:i + columns_per_row]):
            with cols[col_index]:
                if col_name in features_to_encode:
                    input_data[col_name] = st.selectbox(f"Select {col_name}", df[col_name].unique())
                else:
                    input_data[col_name] = st.number_input(f"Enter {col_name}", min_value=0, value=0)

    if st.button("Detect Attack"):
        result = detect_attack(input_data)
        attack_types = ["Normal", "DoS", "Probe", "U2R", "R2L"]
        st.markdown(f""" ##### The predicted type of traffic is: :green[{attack_types[result]}]""")

        binary_predictions = binary_model.predict(binary_val_X)
        accuracy = accuracy_score(binary_val_y, binary_predictions)
        precision = precision_score(binary_val_y, binary_predictions, average='weighted')
        recall = recall_score(binary_val_y, binary_predictions, average='weighted')

        st.markdown(f""" 
                ##### Model Accuracy: {accuracy}
                ##### Model Precision: {precision}
                ##### Model Recall: {recall}
        """)

        st.markdown("**Confusion Matrix:**")
        conf_matrix = confusion_matrix(binary_val_y, binary_predictions)
        fig, ax = plt.subplots()
        sns.heatmap(conf_matrix, annot=True, fmt='d', cmap="YlGnBu", ax=ax)
        st.pyplot(fig)