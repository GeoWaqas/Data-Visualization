import streamlit as st
import pandas as pd

st.write("hello world")

df = pd.read_csv("Bastor Craton.csv")
st.dataframe(df)
