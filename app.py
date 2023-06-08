import streamlit as st
import joblib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("model inference")



model = joblib.load("model.pkl")
scalar = joblib.load("scalar.pkl")
df = pd.read_csv(r"C:\Users\Dhananjay\Desktop\streamlit_code\Social_Network_Ads.csv")

st.write(df)

a = st.text_input("num1:")
b = st.text_input("num2:")

button = st.button("add")
if(button):
    st.write(int(a)+int(b))

    


