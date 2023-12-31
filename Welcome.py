import streamlit as st
import pandas as pd
import os

filename_list = []
for i in os.listdir():
  if i.endswith("csv"):
    filename_list.append(i)



st.write("My Data Visualization Website")

selection = st.multiselect("Select files" , filename_list, filename_list[0])
df_list=[]
for file in filename_list:
  df = pd.read_csv(file)
  df_list.append(file)
st.write(df_list)
st.dataframe(df)

el_list = df.columns.tolist() [27:80]
x_axis = st.selectbox("select X element", el_list)
y_axis = st.selectbox("select Y element", el_list)

from bokeh.plotting import figure
p= figure(x_axis_label = x_axis, y_axis_label = y_axis)

for i in df_list:
  p.scatter((df[i][x_axis]/10000), (df[i][y_axis]/10000, legend_label = df_list[i]))


st.bokeh_chart(p, use_container_width=True)
