import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Task 2 - Data Analysis & Visualization")

df = pd.read_csv("sales.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

st.subheader("Sales Data")
st.dataframe(df)

st.subheader("Dataset Information")
st.write("Rows:", df.shape[0])
st.write("Columns:", df.shape[1])

# Find sales column automatically
sales_col = None

for col in df.columns:
    if "sale" in col.lower():
        sales_col = col
        break

# Find product column automatically
product_col = None

for col in df.columns:
    if "product" in col.lower():
        product_col = col
        break

if sales_col is None:
    st.error("Sales column nahi mila.")
    st.write("Available columns:", list(df.columns))
    st.stop()

st.subheader("Key Information")

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", df[sales_col].sum())

col2.metric("Total Records", len(df))

if product_col:
    col3.metric("Unique Products", df[product_col].nunique())

st.subheader("Sales by Product")

if product_col:
    product_sales = df.groupby(product_col)[sales_col].sum()
    st.bar_chart(product_sales)

st.subheader("Sales Distribution")

fig, ax = plt.subplots()
ax.hist(df[sales_col], bins=10)
ax.set_xlabel(sales_col)
ax.set_ylabel("Frequency")
ax.set_title("Sales Distribution")
st.pyplot(fig)

st.subheader("Correlation Heatmap")

numeric_df = df.select_dtypes(include="number")

if len(numeric_df.columns) >= 2:
    fig, ax = plt.subplots()
    sns.heatmap(numeric_df.corr(), annot=True, ax=ax)
    st.pyplot(fig)
else:
    st.info("Heatmap ke liye enough numeric columns nahi hain.")

st.success("Task 2 completed successfully!")