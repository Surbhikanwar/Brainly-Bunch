from flask import Flask, request, jsonify, render_template
import pickle
from lime.lime_text import LimeTextExplainer

app = Flask(__name__)
from flask_cors import CORS
CORS(app)



# Load model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def predict_proba_wrapper(texts):
    vec = vectorizer.transform(texts)
    return model.predict_proba(vec)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        review = data.get("review", "")

        # Predict
        review_vec = vectorizer.transform([review])
        prediction = model.predict(review_vec)[0]
        label = "Suspicious" if prediction == 1 else "Genuine"

        # Explain with LIME
        explainer = LimeTextExplainer(class_names=["Genuine", "Suspicious"])
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