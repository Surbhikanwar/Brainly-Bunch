import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os
import pandas as pd  # ✅ This line is required

dataset_path = os.getenv("DATASET_PATH", "dataset/fake_reviews.csv")
df = pd.read_csv(dataset_path)

print(df.head())

# Load dataset
# df = pd.read_csv("dataset/fake_reviews.csv")
print("Available columns:", df.columns.tolist())

# Try to automatically detect review and label columns
possible_review_cols = ["review", "reviews", "text", "review_text", "reviews.text"]
possible_label_cols = ["label", "target", "is_fake"]

review_col = next((col for col in possible_review_cols if col in df.columns), None)
label_col = next((col for col in possible_label_cols if col in df.columns), None)

if review_col is None or label_col is None:
    raise ValueError("Dataset must contain a review column (e.g. 'review') and a label column (e.g. 'label').")

X = df[review_col].astype(str)
y = df[label_col]

# Vectorize
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vec, y)

# Save model and vectorizer
os.makedirs("models", exist_ok=True)

with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model and vectorizer saved to models/")
