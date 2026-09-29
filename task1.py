import pandas as pd

# ==========================================================
# TASK 1: DATA IMMERSION & WRANGLING
# ==========================================================

print("==============================================")
print("       TASK 1 - DATA IMMERSION & WRANGLING")
print("==============================================")


# ==========================================================
# PART 1: DATA ACCESS & FAMILIARIZATION
# ==========================================================

print("\n\n========== PART 1: DATA ACCESS & FAMILIARIZATION ==========")

# Load dataset
df = pd.read_csv("sales.csv")

print("\nOriginal Dataset:")
print(df)

# Display first 5 records
print("\nFirst 5 Records:")
print(df.head())

# Display number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns.tolist())

# Display data types
print("\nData Types:")
print(df.dtypes)

# Display complete information
print("\nDataset Information:")
df.info()


# ==========================================================
# PART 2: DATA QUALITY ASSESSMENT
# ==========================================================

print("\n\n========== PART 2: DATA QUALITY ASSESSMENT ==========")

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())

# Basic statistics
print("\nBasic Statistical Summary:")
print(df.describe())

# Check unique values
print("\nUnique Values:")
for column in df.columns:
    print(column, ":", df[column].nunique())


# ==========================================================
# PART 3: DATA CLEANING & TRANSFORMATION
# ==========================================================

print("\n\n========== PART 3: DATA CLEANING & TRANSFORMATION ==========")

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Date column into proper date format
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Remove extra spaces from text columns
df["Product"] = df["Product"].str.strip()
df["Category"] = df["Category"].str.strip()
df["Region"] = df["Region"].str.strip()

# Handle missing values
df["Product"] = df["Product"].fillna("Unknown")
df["Category"] = df["Category"].fillna("Unknown")
df["Region"] = df["Region"].fillna("Unknown")

df["Quantity"] = df["Quantity"].fillna(0)
df["Price"] = df["Price"].fillna(df["Price"].mean())

# Feature Engineering
# Create a new Total_Sales column
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Display cleaned data
print("\nCleaned Dataset:")
print(df)

# Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Check duplicates after cleaning
print("\nDuplicates After Cleaning:")
print(df.duplicated().sum())


# ==========================================================
# PART 4: SAVE CLEANED DATASET
# ==========================================================

print("\n\n========== PART 4: SAVING CLEANED DATA ==========")

df.to_csv("cleaned_sales.csv", index=False)

print("Cleaned dataset saved successfully!")
print("File Name: cleaned_sales.csv")


# ==========================================================
# PART 5: CREATE DATA DICTIONARY
# ==========================================================

print("\n\n========== PART 5: DATA DICTIONARY ==========")

data_dictionary = pd.DataFrame({
    "Column Name": df.columns,
    "Data Type": [str(df[column].dtype) for column in df.columns],
    "Description": [
        "Unique identification number of the order",
        "Date on which the order was placed",
        "Name of the product sold",
        "Category of the product",
        "Number of units sold",
        "Price of one unit of the product",
        "Region where the order was made",
        "Total sales amount calculated using Quantity multiplied by Price"
    ]
})

# Save data dictionary as Excel
data_dictionary.to_excel(
    "data_dictionary.xlsx",
    index=False
)

print("Data dictionary created successfully!")
print("File Name: data_dictionary.xlsx")


# ==========================================================
# FINAL RESULT
# ==========================================================

print("\n\n==============================================")
print("          TASK 1 COMPLETED SUCCESSFULLY")
print("==============================================")

print("\nFiles Created:")
print("1. cleaned_sales.csv")
print("2. data_dictionary.xlsx")
print("\nCleaning script: Task1.py")

print("\nThank You!")
