import pandas as pd

# Load the dataset
df = pd.read_csv(r'dataset\fake_reviews.csv', on_bad_lines='skip')

# Keep only relevant columns that exist
df = df[['reviews.text', 'reviews.rating']]

# Drop rows with missing reviews or ratings
df.dropna(subset=['reviews.text', 'reviews.rating'], inplace=True)

# Convert ratings to numbers if needed
df['reviews.rating'] = pd.to_numeric(df['reviews.rating'], errors='coerce')
df.dropna(subset=['reviews.rating'], inplace=True)

# Label reviews: 1 = Genuine (rating >= 4), 0 = Fake (rating <= 2)
def label_review(rating):
    if rating >= 4:
        return 1
    elif rating <= 2:
        return 0
    else:
        return None

df['label'] = df['reviews.rating'].apply(label_review)

# Drop neutral reviews (rating = 3 or None)
df.dropna(subset=['label'], inplace=True)

# Final format
df = df[['reviews.text', 'label']]
df.rename(columns={'reviews.text': 'review'}, inplace=True)

# Save cleaned dataset
df.to_csv("dataset/fake_reviews.csv", index=False)
print(f"✅ Saved {df.shape[0]} labeled reviews to 'dataset/fake_reviews.csv'")
