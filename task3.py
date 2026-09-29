import streamlit as st
import pandas as pd
import plotly.express as px
import os

# =========================================================
# TASK 3 - DEEP-DIVE ANALYSIS & INTERACTIVE DASHBOARD
# =========================================================

st.set_page_config(
    page_title="Sales Interactive Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.title("📊 Sales Deep-Dive Analysis & Interactive Dashboard")
st.write("Task 3 - KPI Analysis, Deep-Dive Analysis and Interactive Dashboard")

# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------

file_name = "cleaned_sales.csv"

if not os.path.exists(file_name):
    st.error("cleaned_sales.csv not found!")
    st.stop()

df = pd.read_csv(file_name)

# ---------------------------------------------------------
# CLEAN COLUMN NAMES
# ---------------------------------------------------------

df.columns = df.columns.str.strip()

# ---------------------------------------------------------
# FIND IMPORTANT COLUMNS
# ---------------------------------------------------------

sales_column = None
product_column = None
category_column = None
quantity_column = None

for col in df.columns:

    name = col.lower().strip()

    if name in [
        "total_sales",
        "total sales",
        "sales",
        "revenue",
        "amount",
        "total_amount"
    ]:
        sales_column = col

    if name in [
        "product",
        "product_name",
        "product name"
    ]:
        product_column = col

    if name in [
        "category",
        "product_category",
        "product category"
    ]:
        category_column = col

    if name in [
        "quantity",
        "qty"
    ]:
        quantity_column = col


# ---------------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------------

st.sidebar.header("🔎 Dashboard Filters")

filtered_df = df.copy()

# Category filter
if category_column:

    categories = sorted(
        df[category_column].dropna().unique().tolist()
    )

    selected_categories = st.sidebar.multiselect(
        "Select Category",
        categories,
        default=categories
    )

    filtered_df = filtered_df[
        filtered_df[category_column].isin(selected_categories)
    ]


# Product filter
if product_column:

    products = sorted(
        filtered_df[product_column].dropna().unique().tolist()
    )

    selected_products = st.sidebar.multiselect(
        "Select Product",
        products,
        default=products
    )

    filtered_df = filtered_df[
        filtered_df[product_column].isin(selected_products)
    ]


# ---------------------------------------------------------
# KPI SECTION
# ---------------------------------------------------------

st.subheader("📌 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

# KPI 1 - Total Sales
with col1:

    if sales_column:
        total_sales = filtered_df[sales_column].sum()

        st.metric(
            "Total Sales",
            f"{total_sales:,.2f}"
        )

    else:
        st.metric(
            "Total Sales",
            "N/A"
        )


# KPI 2 - Average Sales
with col2:

    if sales_column and len(filtered_df) > 0:

        average_sales = filtered_df[sales_column].mean()

        st.metric(
            "Average Sales",
            f"{average_sales:,.2f}"
        )

    else:
        st.metric(
            "Average Sales",
            "N/A"
        )


# KPI 3 - Number of Products
with col3:

    if product_column:

        total_products = filtered_df[product_column].nunique()

        st.metric(
            "Unique Products",
            total_products
        )

    else:
        st.metric(
            "Unique Products",
            "N/A"
        )


# KPI 4 - Number of Categories
with col4:

    if category_column:

        total_categories = filtered_df[category_column].nunique()

        st.metric(
            "Categories",
            total_categories
        )

    else:
        st.metric(
            "Categories",
            "N/A"
        )


# =========================================================
# DEEP-DIVE ANALYSIS
# =========================================================

st.divider()

st.header("🔍 Deep-Dive Analysis")


# ---------------------------------------------------------
# SALES BY CATEGORY
# ---------------------------------------------------------

if category_column and sales_column:

    st.subheader("Sales by Category")

    category_sales = (
        filtered_df
        .groupby(category_column)[sales_column]
        .sum()
        .reset_index()
        .sort_values(
            sales_column,
            ascending=False
        )
    )

    fig_category = px.bar(
        category_sales,
        x=category_column,
        y=sales_column,
        title="Sales by Category",
        text_auto=True
    )

    st.plotly_chart(
        fig_category,
        use_container_width=True
    )


# ---------------------------------------------------------
# TOP PRODUCTS
# ---------------------------------------------------------

if product_column and sales_column:

    st.subheader("Top Products by Sales")

    product_sales = (
        filtered_df
        .groupby(product_column)[sales_column]
        .sum()
        .reset_index()
        .sort_values(
            sales_column,
            ascending=False
        )
        .head(10)
    )

    fig_product = px.bar(
        product_sales,
        x=sales_column,
        y=product_column,
        orientation="h",
        title="Top 10 Products by Sales",
        text_auto=True
    )

    st.plotly_chart(
        fig_product,
        use_container_width=True
    )


# ---------------------------------------------------------
# QUANTITY ANALYSIS
# ---------------------------------------------------------

if quantity_column and product_column:

    st.subheader("Product Quantity Analysis")

    quantity_data = (
        filtered_df
        .groupby(product_column)[quantity_column]
        .sum()
        .reset_index()
        .sort_values(
            quantity_column,
            ascending=False
        )
        .head(10)
    )

    fig_quantity = px.bar(
        quantity_data,
        x=product_column,
        y=quantity_column,
        title="Top Products by Quantity"
    )

    fig_quantity.update_layout(
        xaxis_tickangle=-45
    )

    st.plotly_chart(
        fig_quantity,
        use_container_width=True
    )


# =========================================================
# RELATIONSHIP ANALYSIS
# =========================================================

st.divider()

st.header("📈 Relationship Analysis")

numeric_columns = filtered_df.select_dtypes(
    include="number"
).columns.tolist()

if len(numeric_columns) >= 2:

    col_a, col_b = st.columns(2)

    with col_a:

        x_axis = st.selectbox(
            "Select X-axis",
            numeric_columns,
            index=0
        )

    with col_b:

        y_axis = st.selectbox(
            "Select Y-axis",
            numeric_columns,
            index=1
        )

    fig_scatter = px.scatter(
        filtered_df,
        x=x_axis,
        y=y_axis,
        title=f"{x_axis} vs {y_axis}",
        trendline="ols"
    )

    st.plotly_chart(
        fig_scatter,
        use_container_width=True
    )


# =========================================================
# CORRELATION
# =========================================================

st.subheader("Correlation Analysis")

if len(numeric_columns) >= 2:

    correlation = filtered_df[
        numeric_columns
    ].corr()

    fig_corr = px.imshow(
        correlation,
        text_auto=True,
        title="Correlation Matrix"
    )

    st.plotly_chart(
        fig_corr,
        use_container_width=True
    )


# =========================================================
# DATA TABLE
# =========================================================

st.divider()

st.header("📋 Filtered Dataset")

st.write(
    "Number of records:",
    len(filtered_df)
)

st.dataframe(
    filtered_df,
    use_container_width=True
)


# =========================================================
# KPI BUSINESS INTERPRETATION
# =========================================================

st.divider()

st.header("💡 Key Business Insights")

if sales_column and len(filtered_df) > 0:

    total_sales = filtered_df[sales_column].sum()
    average_sales = filtered_df[sales_column].mean()

    st.write(
        f"• Total sales in the selected data: "
        f"{total_sales:,.2f}"
    )

    st.write(
        f"• Average sales per record: "
        f"{average_sales:,.2f}"
    )

if category_column and sales_column:

    category_sales = (
        filtered_df
        .groupby(category_column)[sales_column]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    if len(category_sales) > 0:

        top_category = category_sales.index[0]

        st.write(
            f"• Highest-sales category: "
            f"{top_category}"
        )

if product_column and sales_column:

    product_sales = (
        filtered_df
        .groupby(product_column)[sales_column]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    if len(product_sales) > 0:

        top_product = product_sales.index[0]

        st.write(
            f"• Highest-sales product: "
            f"{top_product}"
        )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.success(
    "TASK 3 DASHBOARD READY"
)

st.write(
    "Interactive dashboard created using Python, "
    "Pandas, Plotly and Streamlit."
)