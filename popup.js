document.getElementById("checkBtn").addEventListener("click", async () => {
  const review = document.getElementById("reviewInput").value.trim();
  const resultDiv = document.getElementById("result");
  resultDiv.innerText = "Checking...";

  if (!review) {
    resultDiv.innerText = "Please enter a review!";
    return;
  }

  try {
    const res = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ review })
    });

    const data = await res.json();

    const prediction = data.prediction || "Unknown";
    const confidence = data.confidence !== undefined ? Math.round(data.confidence * 100) + "%" : "N/A";
    const trust = data.trust_score !== undefined ? data.trust_score : "N/A";
    const language = data.language || "Unknown";

    resultDiv.innerText = `
Prediction: ${prediction} (${confidence} confident)
Trust Score: ${trust}
Language: ${language}
    `.trim();

  } catch (err) {
    resultDiv.innerText = "Error connecting to server.";
    console.error(err);
  }
});
