import streamlit as st
import pandas as pd
import numpy as np

st.title("🩺 Diabetes Classification App")

st.write("Enter patient data to predict diabetes. (Demo version)")

# Example inputs
pregnancies = st.number_input("Pregnancies", 0, 20, 1)
glucose = st.number_input("Glucose", 0, 200, 100)
bp = st.number_input("Blood Pressure", 0, 150, 70)
skin = st.number_input("Skin Thickness", 0, 100, 20)
insulin = st.number_input("Insulin", 0, 900, 80)
bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
age = st.number_input("Age", 1, 120, 30)

# Fake prediction (replace with trained model later)
if st.button("Predict"):
    result = np.random.choice(["Diabetic", "Not Diabetic"])
    st.success(f"Prediction: {result}")
