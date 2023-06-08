import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("Product Purchase Prediction")

model = joblib.load("regressor.pkl")
scaler = joblib.load("scaler.pkl")

age = st.number_input("Enter age: ")
salary = st.number_input("Enter salary: ")

btn = st.button("Predict")

if btn:
    dp_scaled = scaler.transform([[age,salary]])

    prediction = model.predict(dp_scaled)
    if round(prediction[0]) == 1:
        st.write("Prediction: Purchased")
    else:
        st.write("Prediction: Not Purchased")
    