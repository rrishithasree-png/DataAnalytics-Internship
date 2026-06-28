import pandas as pd

# ==========================================
# STEP 1: Load the Cleaned Dataset
# ==========================================
df = pd.read_excel("../Dataset/Cleaned_Sales_Dataset.xlsx")

print("=" * 60)
print("FEATURE ENGINEERING")
print("=" * 60)

# ==========================================
# STEP 2: Check Data Types
# ==========================================
print("\nCurrent Data Types:")
print(df.dtypes)

# ==========================================
# STEP 3: Convert Order_Date (Safety Check)
# ==========================================
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# ==========================================
# STEP 4: Create New Date Columns
# ==========================================
df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month
df["Month_Name"] = df["Order_Date"].dt.month_name()
df["Quarter"] = df["Order_Date"].dt.quarter
df["Day"] = df["Order_Date"].dt.day
df["Day_Name"] = df["Order_Date"].dt.day_name()

# ==========================================
# STEP 5: Display New Columns
# ==========================================
print("\nNew Date Columns Added Successfully!\n")

print(df[[
    "Order_Date",
    "Year",
    "Month",
    "Month_Name",
    "Quarter",
    "Day",
    "Day_Name"
]].head())

# ==========================================
# STEP 6: Save Enhanced Dataset
# ==========================================
df.to_excel(
    "../Dataset/Enhanced_Sales_Dataset.xlsx",
    index=False
)

print("\n" + "=" * 60)
print("Enhanced dataset saved successfully!")
print("File: Enhanced_Sales_Dataset.xlsx")
print("=" * 60)