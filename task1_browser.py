import streamlit as st
import pandas as pd

st.title("Task 1 - Data Cleaning & Exploration")

df = pd.read_csv("sales.csv")

st.subheader("Original Sales Data")
st.dataframe(df)

st.subheader("Dataset Information")
st.write("Rows:", df.shape[0])
st.write("Columns:", df.shape[1])

st.subheader("First 5 Records")
st.dataframe(df.head())

st.subheader("Cleaned Sales Data")

cleaned_file = "cleaned_sales.csv"

try:
    cleaned_df = pd.read_csv(cleaned_file)
    st.dataframe(cleaned_df)
except FileNotFoundError:
    st.warning("cleaned_sales.csv not found.")

st.success("Task 1 completed successfully!")