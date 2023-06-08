import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Social_Network_Ads.csv")



st.title("Hello world")
n1 = st.text_input(label="name")

btn = st.button(label="submit")
if btn:
    st.write("Hello",n1)

num1 =st.number_input(label="Enter num1")
num2 = st.number_input(label="Enter num2")
btn1 = st.button(label="Addition")
if btn1:
    st.write("Addition:",num1+num2)

figure = plt.figure(figsize=[10,10])
sns.heatmap(df.corr(),annot=True,cmap='crest')


st.dataframe(df.corr())
st.pyplot(figure)
figure = px.line(df['Age'])
st.plotly_chart(figure)

st.image('Image_10.png')
file = st.file_uploader(label='File')
if file is not None:
    st.write(file)
    df2=pd.read_csv(file)
    st.dataframe(df2)
