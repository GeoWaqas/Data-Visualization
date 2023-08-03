import streamlit as st
import pandas as pd
import os

filename_list = []
for i in os.listdir():
  if i.endswith("csv"):
    filename_list.append(i)



st.write("My Data Visualization Website")

selection = st.multiselect("Select files" , filename_list)

df = pd.read_csv(selection)
st.dataframe(df)

el_list = df.columns.tolist() [27:80]
x_axis = st.selectbox("select x elements", el_list)
y_axis = st.selectbox("select y elements", el_list)


