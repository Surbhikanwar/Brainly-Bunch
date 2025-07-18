import streamlit as st
import pickle
import pickle

# Load your trained model
with open("model/honesta_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load the model pipeline
with open("model/honesta_model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.set_page_config(page_title="Honesta - Review Detector", page_icon="🧐")
st.title("Honesta: Fake Review Detection")

# Input box
review = st.text_area("Enter a product review:")

# Predict button
if st.button("Check Review"):
    if review.strip() == "":
        st.warning("Please enter a review first!")
    else:
        prediction = model.predict([review])[0]
        if prediction == 1:
            st.success("This review is likely GENUINE.")
        else:
            st.error("This review is likely FAKE.")
