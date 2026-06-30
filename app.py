import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("model.pkl")

# Page configuration
st.set_page_config(page_title="Student Placement Package Prediction", page_icon="🎓")

# Title
st.title("🎓 Student Placement Package Prediction System")
st.write("Enter the student details below to predict the salary package.")

# User Input
gender = st.selectbox("Gender", ["Male", "Female"])

ssc_p = st.number_input("SSC Percentage", min_value=0.0, max_value=100.0, value=60.0)

ssc_b = st.selectbox("SSC Board", ["Central", "Others"])

hsc_p = st.number_input("HSC Percentage", min_value=0.0, max_value=100.0, value=60.0)

hsc_b = st.selectbox("HSC Board", ["Central", "Others"])

hsc_s = st.selectbox("HSC Stream", ["Science", "Commerce", "Arts"])

degree_p = st.number_input("Degree Percentage", min_value=0.0, max_value=100.0, value=65.0)

degree_t = st.selectbox("Degree Type", ["Sci&Tech", "Comm&Mgmt", "Others"])

workex = st.selectbox("Work Experience", ["Yes", "No"])

etest_p = st.number_input("Employability Test Percentage", min_value=0.0, max_value=100.0, value=70.0)

specialisation = st.selectbox("Specialisation", ["Mkt&HR", "Mkt&Fin"])

mba_p = st.number_input("MBA Percentage", min_value=0.0, max_value=100.0, value=65.0)

status = st.selectbox("Placement Status", ["Placed", "Not Placed"])

# Encoding
gender = 1 if gender == "Male" else 0
ssc_b = 0 if ssc_b == "Central" else 1
hsc_b = 0 if hsc_b == "Central" else 1

stream_map = {
    "Arts": 0,
    "Commerce": 1,
    "Science": 2
}
hsc_s = stream_map[hsc_s]

degree_map = {
    "Comm&Mgmt": 0,
    "Others": 1,
    "Sci&Tech": 2
}
degree_t = degree_map[degree_t]

workex = 1 if workex == "Yes" else 0
specialisation = 1 if specialisation == "Mkt&HR" else 0
status = 1 if status == "Placed" else 0

# Prediction
if st.button("Predict Package"):
    input_data = pd.DataFrame(
        [[gender, ssc_p, ssc_b, hsc_p, hsc_b,
          hsc_s, degree_p, degree_t, workex,
          etest_p, specialisation, mba_p, status]],
        columns=[
            "gender", "ssc_p", "ssc_b", "hsc_p", "hsc_b",
            "hsc_s", "degree_p", "degree_t", "workex",
            "etest_p", "specialisation", "mba_p", "status"
        ]
    )

    prediction = model.predict(input_data)

    st.success(f"🎉 Predicted Salary Package: ₹ {prediction[0]:,.2f}")
