# Save this as app.py
import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open(r"C:\Users\yash1\OneDrive\Desktop\MedicalInsuranceCost\.ipynb_checkpoints\rf_model.pkl", "rb"))
st.title("Medical Insurance Cost Prediction")

# Input fields
age = st.number_input("Age", 18, 100)
sex = st.selectbox("Gender", ['Male', 'Female'])
bmi = st.number_input("BMI", 10.0, 50.0)
children = st.slider("Number of Children", 0, 5)
smoker = st.selectbox("Smoker", ['Yes', 'No'])
region = st.selectbox("Region", ['southeast', 'southwest', 'northeast', 'northwest'])

# Preprocess inputs
sex = 0 if sex == 'Male' else 1
smoker = 1 if smoker == 'Yes' else 0
region_southeast = region == 'southeast'
region_southwest = region == 'southwest'
region_northwest = region == 'northwest'

input_data = np.array([[age, sex, bmi, children, smoker,
                        int(region_northwest), int(region_southeast), int(region_southwest)]])

# Predict
if st.button("Predict Insurance Cost"):
    result = model.predict(input_data)
    st.success(f"Estimated Insurance Cost: ${result[0]:.2f}")
