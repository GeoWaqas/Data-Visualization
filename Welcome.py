import streamlit as st
import pandas as pd
import os
from bokeh.plotting import figure, show
from bokeh.io import output_notebook

filename_list = []
for i in os.listdir():
  if i.endswith("csv"):
    filename_list.append(i)



st.write("My Data Visualization Website")

selection = st.selectbox("Select files" , filename_list)

df = pd.read_csv(selection)
st.dataframe(df)

el_list = df.columns.tolist() [27:80]
x_axis = st.selectbox("select x elements", el_list)
y_axis = st.selectbox("select y elements", el_list)

df = pd.read_csv("Bastar Craton.csv")

output_notebook()

p= figure(x_axis_label = "x", y_axis_label = "y")
p.triangle(df["Mg"]/10000, df["Si"]/10000)
p.circle(df["Al"]/10000, df["Si"]/10000)
p.square(df["K"]/10000, df["Si"]/10000)
show(p)

