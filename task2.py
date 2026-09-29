import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import os

print("=" * 60)
print("          TASK 2 - EDA & BUSINESS INTELLIGENCE")
print("=" * 60)

# ---------------------------------------------------------
# LOAD CLEANED DATASET
# ---------------------------------------------------------

file_name = "cleaned_sales.csv"

if not os.path.exists(file_name):
    print("\nERROR: cleaned_sales.csv not found!")
    print("Please keep cleaned_sales.csv in the same folder as task2.py")
    exit()

df = pd.read_csv(file_name)

print("\nDataset loaded successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())


# =========================================================
# PART 1: DESCRIPTIVE STATISTICS & UNIVARIATE ANALYSIS
# =========================================================

print("\n" + "=" * 60)
print("PART 1: DESCRIPTIVE STATISTICS & UNIVARIATE ANALYSIS")
print("=" * 60)

# Numerical summary
print("\n--- Numerical Summary ---")
print(df.describe())

# Data types
print("\n--- Data Types ---")
print(df.dtypes)

# Missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())


# ---------------------------------------------------------
# Find numerical and categorical columns
# ---------------------------------------------------------

numeric_columns = df.select_dtypes(include="number").columns.tolist()
categorical_columns = df.select_dtypes(include="object").columns.tolist()

print("\nNumerical Columns:")
print(numeric_columns)

print("\nCategorical Columns:")
print(categorical_columns)


# ---------------------------------------------------------
# Categorical value counts
# ---------------------------------------------------------

for column in categorical_columns:
    print("\n---", column, "Value Counts ---")
    print(df[column].value_counts().head(10))


# ---------------------------------------------------------
# HISTOGRAMS
# ---------------------------------------------------------

os.makedirs("task2_outputs", exist_ok=True)

for column in numeric_columns:
    plt.figure(figsize=(8, 5))
    plt.hist(df[column].dropna(), bins=10)
    plt.title("Distribution of " + column)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.tight_layout()

    file_path = "task2_outputs/histogram_" + column + ".png"
    plt.savefig(file_path)
    plt.close()

print("\nHistograms created successfully.")


# ---------------------------------------------------------
# BAR CHARTS FOR CATEGORICAL DATA
# ---------------------------------------------------------

for column in categorical_columns:
    value_counts = df[column].value_counts().head(10)

    plt.figure(figsize=(8, 5))
    value_counts.plot(kind="bar")
    plt.title("Top Categories - " + column)
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()

    file_path = "task2_outputs/bar_" + column + ".png"
    plt.savefig(file_path)
    plt.close()

print("Bar charts created successfully.")


# =========================================================
# PART 2: SQL BUSINESS QUESTIONS
# =========================================================

print("\n" + "=" * 60)
print("PART 2: SQL BUSINESS QUESTIONS")
print("=" * 60)

# Create SQLite database in memory
connection = sqlite3.connect(":memory:")

# Store dataframe as SQL table
df.to_sql("sales", connection, index=False, if_exists="replace")

print("\nSQL table 'sales' created successfully.")


# ---------------------------------------------------------
# Business Question 1
# How many total records are present?
# ---------------------------------------------------------

query1 = """
SELECT COUNT(*) AS total_records
FROM sales;
"""

result1 = pd.read_sql_query(query1, connection)

print("\nBusiness Question 1:")
print("How many total records are present?")
print(result1)


# ---------------------------------------------------------
# Business Question 2
# Total sales / sum of numerical sales column
# ---------------------------------------------------------

sales_column = None

for column in df.columns:
    if column.lower() in [
        "total_sales",
        "total sales",
        "sales",
        "revenue",
        "amount",
        "total_amount"
    ]:
        sales_column = column
        break

if sales_column:

    query2 = f"""
    SELECT SUM("{sales_column}") AS total_sales
    FROM sales;
    """

    result2 = pd.read_sql_query(query2, connection)

    print("\nBusiness Question 2:")
    print("What is the total sales/revenue?")
    print(result2)

else:
    print("\nSales column not automatically found.")


# ---------------------------------------------------------
# Business Question 3
# Average sales
# ---------------------------------------------------------

if sales_column:

    query3 = f"""
    SELECT AVG("{sales_column}") AS average_sales
    FROM sales;
    """

    result3 = pd.read_sql_query(query3, connection)

    print("\nBusiness Question 3:")
    print("What is the average sales/revenue?")
    print(result3)


# ---------------------------------------------------------
# Business Question 4
# Sales by category
# ---------------------------------------------------------

category_column = None

for column in df.columns:
    if column.lower() in ["category", "product_category", "product category"]:
        category_column = column
        break

if sales_column and category_column:

    query4 = f"""
    SELECT
        "{category_column}" AS category,
        SUM("{sales_column}") AS total_sales
    FROM sales
    GROUP BY "{category_column}"
    ORDER BY total_sales DESC;
    """

    result4 = pd.read_sql_query(query4, connection)

    print("\nBusiness Question 4:")
    print("Which category generates the highest sales?")
    print(result4)


# ---------------------------------------------------------
# Business Question 5
# Top 5 products by sales
# ---------------------------------------------------------

product_column = None

for column in df.columns:
    if column.lower() in ["product", "product_name", "product name"]:
        product_column = column
        break

if sales_column and product_column:

    query5 = f"""
    SELECT
        "{product_column}" AS product,
        SUM("{sales_column}") AS total_sales
    FROM sales
    GROUP BY "{product_column}"
    ORDER BY total_sales DESC
    LIMIT 5;
    """

    result5 = pd.read_sql_query(query5, connection)

    print("\nBusiness Question 5:")
    print("What are the top 5 products by sales?")
    print(result5)


# ---------------------------------------------------------
# Business Question 6
# Minimum and maximum sales
# ---------------------------------------------------------

if sales_column:

    query6 = f"""
    SELECT
        MIN("{sales_column}") AS minimum_sales,
        MAX("{sales_column}") AS maximum_sales
    FROM sales;
    """

    result6 = pd.read_sql_query(query6, connection)

    print("\nBusiness Question 6:")
    print("What are the minimum and maximum sales?")
    print(result6)


# ---------------------------------------------------------
# Business Question 7
# Number of products/categories
# ---------------------------------------------------------

if product_column:

    query7 = f"""
    SELECT COUNT(DISTINCT "{product_column}") AS unique_products
    FROM sales;
    """

    result7 = pd.read_sql_query(query7, connection)

    print("\nBusiness Question 7:")
    print("How many unique products are present?")
    print(result7)


# =========================================================
# PART 3: MULTIVARIATE ANALYSIS & CORRELATION
# =========================================================

print("\n" + "=" * 60)
print("PART 3: MULTIVARIATE ANALYSIS & CORRELATION")
print("=" * 60)


# ---------------------------------------------------------
# Correlation Matrix
# ---------------------------------------------------------

if len(numeric_columns) >= 2:

    correlation = df[numeric_columns].corr()

    print("\n--- Correlation Matrix ---")
    print(correlation)

    plt.figure(figsize=(10, 7))

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Heatmap")
    plt.tight_layout()

    plt.savefig("task2_outputs/correlation_heatmap.png")
    plt.close()

    print("\nCorrelation heatmap created.")


# ---------------------------------------------------------
# Scatter plots
# ---------------------------------------------------------

if len(numeric_columns) >= 2:

    x_column = numeric_columns[0]
    y_column = numeric_columns[1]

    plt.figure(figsize=(8, 5))

    plt.scatter(
        df[x_column],
        df[y_column],
        alpha=0.6
    )

    plt.title(x_column + " vs " + y_column)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.tight_layout()

    plt.savefig("task2_outputs/scatter_plot.png")
    plt.close()

    print("Scatter plot created.")


# ---------------------------------------------------------
# Pair Plot
# ---------------------------------------------------------

if len(numeric_columns) >= 2:

    selected_columns = numeric_columns[:4]

    pair_data = df[selected_columns].dropna()

    if len(pair_data) > 0:

        sns.pairplot(pair_data)

        plt.savefig("task2_outputs/pair_plot.png")
        plt.close()

        print("Pair plot created.")


# =========================================================
# PART 4: STATIC DASHBOARD KPI SUMMARY
# =========================================================

print("\n" + "=" * 60)
print("PART 4: STATIC DASHBOARD KPI SUMMARY")
print("=" * 60)

total_records = len(df)

print("\nDashboard KPIs")

print("------------------------------")
print("Total Records:", total_records)

if sales_column:

    total_sales = df[sales_column].sum()
    average_sales = df[sales_column].mean()

    print("Total Sales:", round(total_sales, 2))
    print("Average Sales:", round(average_sales, 2))

if product_column:
    print("Unique Products:", df[product_column].nunique())

if category_column:
    print("Unique Categories:", df[category_column].nunique())


# ---------------------------------------------------------
# Create simple KPI dashboard image
# ---------------------------------------------------------

plt.figure(figsize=(12, 7))

plt.axis("off")

plt.text(
    0.5,
    0.90,
    "SALES BUSINESS INTELLIGENCE DASHBOARD",
    ha="center",
    fontsize=20,
    fontweight="bold"
)

plt.text(
    0.20,
    0.65,
    "TOTAL RECORDS\n" + str(total_records),
    ha="center",
    fontsize=16
)

if sales_column:

    plt.text(
        0.50,
        0.65,
        "TOTAL SALES\n" + str(round(df[sales_column].sum(), 2)),
        ha="center",
        fontsize=16
    )

    plt.text(
        0.80,
        0.65,
        "AVERAGE SALES\n" + str(round(df[sales_column].mean(), 2)),
        ha="center",
        fontsize=16
    )

if product_column:

    plt.text(
        0.35,
        0.35,
        "UNIQUE PRODUCTS\n" + str(df[product_column].nunique()),
        ha="center",
        fontsize=16
    )

if category_column:

    plt.text(
        0.65,
        0.35,
        "UNIQUE CATEGORIES\n" + str(df[category_column].nunique()),
        ha="center",
        fontsize=16
    )

plt.savefig(
    "task2_outputs/static_dashboard.png",
    bbox_inches="tight"
)

plt.close()

print("\nStatic dashboard created.")


# =========================================================
# FINAL MESSAGE
# =========================================================

connection.close()

print("\n" + "=" * 60)
print("             TASK 2 COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nOutput files are saved inside:")
print("task2_outputs")

print("\nGenerated:")
print("1. Histograms")
print("2. Bar charts")
print("3. SQL business analysis")
print("4. Correlation heatmap")
print("5. Scatter plot")
print("6. Pair plot")
print("7. Static dashboard")

print("\nThank You!")