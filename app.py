import streamlit as st
import joblib
import pandas as pd
from pathlib import Path

# ---------------- Page Configuration ----------------
st.set_page_config(page_title="Pump Predictor", layout="wide")

# Page background styling
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        background-attachment: fixed;
    }
    section[data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.08);
    }
    h1 {
        text-align: center;
        color: white;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- Load model, encoders, feature columns ----------------
base_path = Path(__file__).parent
model = joblib.load(base_path / "models" / "pump_model.pkl")
encoders_X = joblib.load(base_path / "models" / "encoders_X.pkl")
le_Y = joblib.load(base_path / "models" / "le_Y.pkl")
feature_columns = joblib.load(base_path / "models" / "feature_columns.pkl")

# ---------------- Page Title ----------------
st.markdown("<h1>Pump Functionality Predictor</h1>", unsafe_allow_html=True)

# ---------------- Sidebar Inputs ----------------
st.sidebar.header("Enter Waterpoint Details")

# Numeric features
with st.sidebar.expander("Numeric Features", expanded=False):
    amount_tsh = st.number_input("Amount of water available", 0, 400000, 1000, 100)
    gps_height = st.number_input("Altitude of well (meters)", 0, 3000, 1000, 10)
    population = st.number_input("Population of community", 0, 40000, 100, 10)
    age = st.number_input("Age of water pump (years)", 0, 100, 10, 1)

# Binary features
with st.sidebar.expander("Binary Features", expanded=False):
    public_meeting = st.selectbox("Public Meeting", ["TRUE", "FALSE"])
    permit = st.selectbox("Permit", ["TRUE", "FALSE"])
    public_meeting = 1 if public_meeting == "TRUE" else 0
    permit = 1 if permit == "TRUE" else 0

# Categorical features
with st.sidebar.expander("Categorical Features", expanded=False):
    inputs = {}
    for col in encoders_X.keys():
        categories = encoders_X[col].classes_
        selected = st.selectbox(f"{col.replace('_',' ').title()}", categories)
        inputs[col] = selected

# ---------------- Prepare Input DataFrame ----------------
X_input_list = [amount_tsh, gps_height, population, age, public_meeting, permit]

for col in encoders_X.keys():
    encoded_value = encoders_X[col].transform([inputs[col]])[0]
    X_input_list.append(encoded_value)

# Create DataFrame with exact feature columns
X_input_df = pd.DataFrame([X_input_list], columns=feature_columns)

# ---------------- Predict Button ----------------
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1.5, 1])

with col2:
    predict_clicked = st.button("Predict Pump Status", use_container_width=True)

# ---------------- Prediction & Display ----------------
if predict_clicked:
    prediction = model.predict(X_input_df)
    result = le_Y.inverse_transform(prediction)[0]

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        if result.lower() == "functional":
            st.success(f"✅ The predicted pump functionality is: {result}")
        else:
            st.error(f"❌ The predicted pump functionality is: {result}")
