import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

#  Load real dataset
df = pd.read_csv("fake_reviews.csv")  # Replace with your actual filename
X = df["review_text"]
y = df["label"]

#  Vectorize
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

#  Train model
model = MultinomialNB()
model.fit(X_vec, y)

#  Save model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print(" Real model and vectorizer saved!")
