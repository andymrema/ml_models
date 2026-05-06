Water Pump Functionality Prediction

Project Overview

This project builds a Machine Learning model to predict the functionality status of water pumps. The model classifies pumps into categories such as functional or non-functional based on operational and environmental features.

The solution includes:

1.Data preprocessing and encoding

2.Model training using a Decision Tree Classifier

3.Model serialization using Joblib

4.Deployment using Streamlit

────────────────────────────

Problem Statement

Access to clean water is highly dependent on properly functioning water pumps. Predicting pump status helps identify areas that require maintenance and resource allocation.

This project uses supervised machine learning techniques to predict pump functionality using structured tabular data.

────────────────────────────

Machine Learning Approach

Algorithm Used:
Decision Tree Classifier

Encoding Method:
Label Encoding for categorical variables

Target Encoding:
LabelEncoder

Model Persistence:
Joblib (.pkl format)

Steps Performed:

1.Handling missing values

2.Encoding categorical features

3.Training the model

4.Saving the trained model

5.Building a Streamlit interface for live predictions

────────────────────────────

Technologies Used

1.Python

2.Pandas

3.NumPy

4.Scikit-learn

5.Joblib

6.Streamlit

────────────────────────────

Project Structure

app.py
models/
pump_model.pkl
encoders_X.pkl
feature_columns.pkl
le_Y.pkl
requirements.txt
README.md

────────────────────────────

How to Run Locally

Step 1: Install dependencies
pip install -r requirements.txt

Step 2: Run the Streamlit application
streamlit run app.py

────────────────────────────

Live Application

Streamlit App URL:
https://mlproject-jabjhfbfb2zfckuvuk5zkd.streamlit.app/

────────────────────────────

Features of the Application;

1.Interactive sidebar inputs

2.Automatic categorical encoding

3.Real-time prediction

4.Clean and user-friendly interface

5.Deployed on Streamlit Community Cloud

────────────────────────────

Model Output

The model predicts:

Functional

Non-Functional

────────────────────────────

Author

– Andrew Mrema
