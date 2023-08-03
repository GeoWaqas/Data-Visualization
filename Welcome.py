import streamlit as st
import pandas as pd
import os

filename_list = []
for i in os.listdir():
  if i.endswith("csv"):
    filename_list.append(i)



st.write("My Data Visualization Website")

selection = st.selectbox("Select files" , filename_list)

df = pd.read_csv(selection)
st.dataframe(df)

el_list = df.columns.tolist() [27:80]
x_axis = st.selectbox("select X element", el_list)
y_axis = st.selectbox("select Y element", el_list)


from bokeh.plotting import figure

df1 = pd.read_csv("Bastar Craton.csv")

p= figure(x_axis_label = "x", y_axis_label = "y")
p.triangle(df1["Mg"]/10000, df1["Si"]/10000)


st.bokeh_chart(p, use_container_width=True)
