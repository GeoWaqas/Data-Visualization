import streamlit as st
import pandas as pd

st.write("hello world")

df = pd.read_csv("Emeishan.csv")
st.dataframe(df)
