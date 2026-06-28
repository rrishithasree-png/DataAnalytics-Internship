import pandas as pd

# ==========================================
# STEP 1: Load the Excel Dataset
# ==========================================
df = pd.read_excel(
    "../Dataset/ApexPlanet_DataAnalytics_Dataset.xlsx",
    sheet_name="Sales_Dataset"
)

# ==========================================
# STEP 2: Display Dataset Before Cleaning
# ==========================================
print("=" * 50)
print("BEFORE CLEANING")
print("=" * 50)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# ==========================================
# STEP 3: Convert Order_Date to Date Format
# ==========================================
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("\nUpdated Data Type of Order_Date:")
print(df["Order_Date"].dtype)

# ==========================================
# STEP 4: Fill Missing Values in Age
# ==========================================
average_age = df["Age"].mean()

print("\nAverage Age:")
print(average_age)

df["Age"] = df["Age"].fillna(average_age)

# ==========================================
# STEP 5: Fill Missing Values in City
# ==========================================
most_common_city = df["City"].mode()[0]

print("\nMost Common City:")
print(most_common_city)

df["City"] = df["City"].fillna(most_common_city)

# ==========================================
# STEP 6: Verify Cleaning
# ==========================================
print("\n" + "=" * 50)
print("AFTER CLEANING")
print("=" * 50)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# ==========================================
# STEP 7: Save Cleaned Dataset
# ==========================================
df.to_excel(
    "../Dataset/Cleaned_Sales_Dataset.xlsx",
    index=False
)

print("\n✅ Cleaned dataset saved successfully!")
print("📁 File Name: Cleaned_Sales_Dataset.xlsx")
print("📂 Location: Dataset folder")