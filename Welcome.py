import streamlit as st
import pandas as pd

st.write("hello world")

df = pd.read_csv("Emeishan.csv")
st.dataframe(df)

el_list = df.columns.tolist() [27:80]
st.selectbox("select elements", el_list)
