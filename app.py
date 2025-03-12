import streamlit as st
import joblib
import pandas as pd

# Load the pre-trained model
model = joblib.load('loan_status_predict.pkl')

# Define a function to make predictions
def predict_loan_status(data):
    result = model.predict(data)
    return result[0]

# Create a Streamlit web app
st.title("Loan Status Prediction")

st.sidebar.header("User Input")

# Create input fields in the sidebar
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
married = st.sidebar.radio("Married", ["Yes", "No"])
dependents = st.sidebar.selectbox("Dependents", [0, 1, 2, 3])
education = st.sidebar.radio("Education", ["Graduate", "Not Graduate"])
self_employed = st.sidebar.radio("Self Employed", ["Yes", "No"])
applicant_income = st.sidebar.number_input("Applicant Income")
coapplicant_income = st.sidebar.number_input("Coapplicant Income")
loan_amount = st.sidebar.number_input("Loan Amount")
loan_term = st.sidebar.number_input("Loan Amount Term")
credit_history = st.sidebar.radio("Credit History", ["Good", "Bad"])
property_area = st.sidebar.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Mapping user inputs to numerical values
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0
credit_history = 1 if credit_history == "Good" else 0

# Mapping property area to numerical values
property_area_mapping = {"Urban": 0, "Semiurban": 1, "Rural": 2}
property_area = property_area_mapping[property_area]

# Create a DataFrame from user inputs
user_data = pd.DataFrame({
    'Gender': [gender],
    'Married': [married],
    'Dependents': [dependents],
    'Education': [education],
    'Self_Employed': [self_employed],
    'ApplicantIncome': [applicant_income],
    'CoapplicantIncome': [coapplicant_income],
    'LoanAmount': [loan_amount],
    'Loan_Amount_Term': [loan_term],
    'Credit_History': [credit_history],
    'Property_Area': [property_area]
})

# Check if the user clicked the "Predict" button
if st.sidebar.button("Predict"):
    result = predict_loan_status(user_data)
    if result == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Not Approved")
