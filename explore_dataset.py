import pandas as pd

# Load the dataset
df = pd.read_csv("dataset/fake_reviews.csv")
print(df[df['label'] == 0].head(10))

# Show basic info
print("\n Dataset Info:")
print(df.info())

# Show first 5 rows
print("\n Sample Data:")
print(df.head())

# Check value counts of label column
print("\n Class Distribution:")
print(df['label'].value_counts())

# Optional: See how many null values
print("\n Missing Values:")
print(df.isnull().sum())
