import pandas as pd

# Load Excel dataset
df = pd.read_excel(
    "../Dataset/ApexPlanet_DataAnalytics_Dataset.xlsx",
    sheet_name="Sales_Dataset"
)

print("=" * 50)
print("FIRST 5 ROWS")
print("=" * 50)
print(df.head())

print("\n" + "=" * 50)
print("DATASET INFORMATION")
print("=" * 50)
df.info()

print("\n" + "=" * 50)
print("DATASET SHAPE")
print("=" * 50)
print(df.shape)

print("\n" + "=" * 50)
print("COLUMN NAMES")
print("=" * 50)
print(df.columns)

print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)
print(df.isnull().sum())

print("\n" + "=" * 50)
print("DUPLICATE ROWS")
print("=" * 50)
print(df.duplicated().sum())

print("\n" + "=" * 50)
print("SUMMARY STATISTICS")
print("=" * 50)
print(df.describe())