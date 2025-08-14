import pandas as pd

# Load the dataset (change file name if needed)
df = pd.read_csv("emails.csv")

# Peek at the first few rows
print(df.head())
print(df.info())
print(df.isnull().sum())
