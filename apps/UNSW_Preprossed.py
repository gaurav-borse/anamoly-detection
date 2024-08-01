import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('D:/College Stuff/4th Year 1st Sem/Project/anamoly-detection-app/apps/datasets/UNSW_NB15.csv')

# Perform one-hot encoding for categorical variables
categorical_cols = ['proto', 'service', 'state']
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), categorical_cols)], remainder='passthrough')
X_encoded = ct.fit_transform(data.drop(['attack_cat', 'label'], axis=1))

# Splitting the data into training and testing sets
X = pd.DataFrame(X_encoded.toarray())
y = data['attack_cat']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply SMOTE to address class imbalance
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Initialize and train a Random Forest classifier
rf_classifier = RandomForestClassifier(random_state=42)
rf_classifier.fit(X_train_resampled, y_train_resampled)

# Save the preprocessor, model, and test data
with open('preprocessor.pkl', 'wb') as f:
    pickle.dump(ct, f)
with open('rf_model.pkl', 'wb') as f:
    pickle.dump(rf_classifier, f)
with open('test_data.pkl', 'wb') as f:
    pickle.dump((X_test, y_test), f)
