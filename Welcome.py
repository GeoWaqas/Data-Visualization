import streamlit as st
import pandas as pd
import os

filename_list = []
for i in os.listdir():
  if i.endswith("csv"):
  filename_list.append[i]

st.write(filename_list)

st.write("My First Website")

st.selectbox("select file", filename_list)

df = pd.read_csv("Emeishan.csv")
st.dataframe(df)

el_list = df.columns.tolist() [27:80]
x_axis = st.selectbox("select elements", el_list)
y_axis = st.selectbox("select elements", el_list)

