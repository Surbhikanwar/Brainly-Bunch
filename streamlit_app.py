import streamlit as st
import pandas as pd
import joblib
from utils.preprocess import clean_text
from utils.pattern_detector import detect_burst_reviews, detect_duplicate_phrases
from utils.explainability import explain_prediction

# Load model and vectorizer
model = joblib.load("models/review_classifier.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

st.set_page_config(page_title="ReviewSentinel Streamlit", layout="wide")
st.title("Fake Review Detection Dashboard")

uploaded_file = st.file_uploader("Upload CSV file containing reviews", type=["csv", "tsv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        # Detect review column
        if "review" in df.columns:
            reviews = df["review"].astype(str)
        elif "reviews.text" in df.columns:
            reviews = df["reviews.text"].astype(str)
        else:
            st.error("No column named 'review' or 'reviews.text' found.")
            st.stop()

        # Clean text
        cleaned = reviews.apply(clean_text)
        X = vectorizer.transform(cleaned)
        predictions = model.predict(X)

        # Pattern detection
        burst_flags = detect_burst_reviews(df)
        duplicate_flags = detect_duplicate_phrases(reviews)

        # Build final result DataFrame
        results = pd.DataFrame({
            "Original Review": reviews,
            "Prediction": predictions,
            "Burst Pattern": burst_flags,
            "Duplicate Phrase": duplicate_flags,
            "Reason": [explain_prediction(text) for text in cleaned]
        })

        # Show table
        st.subheader("Review Analysis Result")
        st.dataframe(results, use_container_width=True)

        # Download
        csv = results.to_csv(index=False).encode('utf-8')
        st.download_button("Download Results as CSV", csv, "review_analysis.csv", "text/csv")

    except Exception as e:
        st.error(f"Error processing file: {e}")
