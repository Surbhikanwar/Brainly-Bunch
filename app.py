from flask import Flask, request, jsonify
from lime.lime_text import LimeTextExplainer
from flask_cors import CORS
import joblib
import pickle

app = Flask(__name__)
CORS(app)

# Load model and vectorizer
model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

# LIME needs a probability function
def predict_proba_wrapper(texts):
    vec = vectorizer.transform(texts)
    return model.predict_proba(vec)

@app.route("/")
def home():
    return jsonify({"message": "Fake Review Detection API is running."})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        review = data.get("review", "")

        # Predict
        review_vec = vectorizer.transform([review])
        prediction = model.predict(review_vec)[0]
        label = "Suspicious" if prediction == "fake" else "Genuine"

        # Explain with LIME
        explainer = LimeTextExplainer(class_names=["fake", "genuine"])
        exp = explainer.explain_instance(review, predict_proba_wrapper, num_features=5)
        explanation = [{"word": word, "score": score} for word, score in exp.as_list()]

        return jsonify({
            "prediction": label,
            "explanation": explanation
        })

    except Exception as e:
        print("❌ Error in /predict:", str(e))
        return jsonify({"prediction": "Error", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
