import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("sales_data.csv")

# Display original data
print("Original Data:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Remove duplicate rows
df = df.drop_duplicates()

# Convert city names to uppercase
df['City'] = df['City'].str.upper()

# Convert OrderDate column
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Create new column
df['Customer_Category'] = np.where(
    df['Sales'] > 5000,
    'Premium',
    'Normal'
)

# Save cleaned dataset
df.to_csv("cleaned_sales_data.csv", index=False)

# Display cleaned data
print("\nCleaned Data:")
print(df)

print("\nData Cleaning Completed Successfully")