import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("model.pkl")

# Page configuration
st.set_page_config(
    page_title="Student Placement Package Prediction",
    page_icon="🎓",
    layout="wide"
)

# Title
st.title("🎓 Student Placement Package Prediction System")
st.write("Predict the salary package based on student details.")

# Sidebar
st.sidebar.header("Student Details")

gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
ssc_p = st.sidebar.number_input("SSC Percentage", 0.0, 100.0)
ssc_b = st.sidebar.selectbox("SSC Board", ["Central", "Others"])
hsc_p = st.sidebar.number_input("HSC Percentage", 0.0, 100.0)
hsc_b = st.sidebar.selectbox("HSC Board", ["Central", "Others"])
hsc_s = st.sidebar.selectbox("HSC Stream", ["Science", "Commerce", "Arts"])
degree_p = st.sidebar.number_input("Degree Percentage", 0.0, 100.0)
degree_t = st.sidebar.selectbox("Degree Type", ["Sci&Tech", "Comm&Mgmt", "Others"])
workex = st.sidebar.selectbox("Work Experience", ["Yes", "No"])
etest_p = st.sidebar.number_input("Employability Test Percentage", 0.0, 100.0)
specialisation = st.sidebar.selectbox("Specialisation", ["Mkt&HR", "Mkt&Fin"])
mba_p = st.sidebar.number_input("MBA Percentage", 0.0, 100.0)
status = st.sidebar.selectbox("Placement Status", ["Placed", "Not Placed"])

# Encode categorical values
gender = 1 if gender == "Male" else 0
ssc_b = 0 if ssc_b == "Central" else 1
hsc_b = 0 if hsc_b == "Central" else 1

stream_map = {"Arts": 0, "Commerce": 1, "Science": 2}
hsc_s = stream_map[hsc_s]

degree_map = {"Comm&Mgmt": 0, "Others": 1, "Sci&Tech": 2}
degree_t = degree_map[degree_t]

workex = 1 if workex == "Yes" else 0
specialisation = 1 if specialisation == "Mkt&HR" else 0
status = 1 if status == "Placed" else 0

if st.sidebar.button("Predict Package"):
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

    st.success(f"Predicted Salary Package: ₹ {prediction[0]:,.2f}")
