ReviewSentinel – AI-Powered Fake Review Detector
🚀 Project Overview

ReviewSentinel is an AI-powered system designed to detect and flag suspicious or fake product reviews on e-commerce platforms like Amazon and Flipkart.
Our tool uses Natural Language Processing (NLP), Behavioral Analysis, and Explainable AI (LIME/SHAP) to provide users with:

A Trust Score for each review.

Classification as Genuine, Suspicious, or Fake.

Explanations highlighting why a review was flagged.

We also built a Chrome Extension that works directly on live product pages, alongside a Flask backend with ML integration.

✨ Key Features

🔍 AI-Powered Review Classification – Detect fake vs. genuine reviews in real-time.

📊 Trust Score & Sentiment Analysis – Quantify reliability and overall sentiment.

🖼️ Explainability (XAI) – LIME/SHAP highlights words/phrases influencing decisions.

🧑‍💻 Chrome Extension – Seamlessly integrates with Amazon/Flipkart product pages.

📈 Dashboard – Upload CSV of reviews to visualize:

% Genuine vs. Fake reviews

Sentiment Pie Charts

Pros & Cons Extraction

Time Trend Charts

📑 PDF Report Generator – Export classification summary, trustworthiness score, and reasoning.

🏗️ Tech Stack

Frontend: Chrome Extension (HTML, JS, CSS)

Backend: Flask (Python)

ML/NLP: Scikit-learn, Pandas, TF-IDF, LIME, SHAP

Visualization: Matplotlib, WordCloud, Chart.js

Export: ReportLab (PDF generation)

🔧 How It Works

Review Scraping: Extension extracts reviews from live product pages.

Classification: Reviews are sent to Flask backend → ML model → classified as Genuine / Suspicious / Fake.

Explainability: LIME/SHAP generates human-understandable reasoning.

Visualization: Chrome Extension/Dashboard displays live charts, verdicts & trust scores.

Export Report: Users can generate a PDF report for deeper analysis.

📂 Project Structure
ReviewSentinel/
│── backend/
│   ├── app.py               # Flask server
│   ├── model.pkl            # Trained ML model
│   ├── vectorizer.pkl       # TF-IDF vectorizer
│   ├── explainability/      # LIME/SHAP scripts
│
│── extension/
│   ├── manifest.json        # Chrome extension config
│   ├── content.js           # Scrapes reviews
│   ├── background.js        # Handles API calls
│   ├── popup.html           # User interface
│   ├── popup.js             # Logic for displaying results
│
│── dashboard/
│   ├── app.py               # Flask dashboard
│   ├── templates/           # HTML templates
│   ├── static/              # CSS, JS, Chart.js
│
│── reports/
│   ├── sample_report.pdf    # Example output
│
└── README.md

⚡ Installation & Usage
🔹 Backend Setup
cd backend
pip install -r requirements.txt
python app.py


Server runs on http://127.0.0.1:5000.

🔹 Chrome Extension Setup

Go to chrome://extensions/

Enable Developer Mode

Click Load unpacked → Select extension/ folder

Open Amazon/Flipkart product page → Click Analyze Reviews

🔹 Dashboard Usage
cd dashboard
python app.py


Open http://127.0.0.1:5000 in browser → Upload CSV of reviews.

🎯 Hackathon Value Proposition

Problem: Fake reviews mislead millions of online shoppers.

Solution: An explainable, real-time, AI-powered system to detect and flag suspicious reviews.

USP: Combines Chrome Extension + ML Backend + Explainable AI + Dashboard + PDF Reporting.

📌 Future Scope

🔹 Multilingual review detection (Hindi-English code-switching).

🔹 Temporal & behavioral reviewer profiling.

🔹 Mobile app integration.

🔹 Scaling to multiple e-commerce platforms globally.
