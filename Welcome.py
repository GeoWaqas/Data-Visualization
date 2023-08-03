import streamlit as st
import pandas as pd

st.write("hello world")

df = pd.read_csv("Bastar Craton.csv")
st.dataframe(df)
