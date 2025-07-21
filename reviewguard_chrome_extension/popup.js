document.getElementById("checkBtn").addEventListener("click", async () => {
  const review = document.getElementById("reviewInput").value;
  if (!review.trim()) {
    document.getElementById("result").innerText = "Please enter a review!";
    return;
  }

  try {
    const res = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ review })
    });

    const data = await res.json();
    document.getElementById("result").innerText = `Prediction: ${data.prediction}`;
  } catch (err) {
    document.getElementById("result").innerText = "Error: Could not connect to the server.";
    console.error(err);
  }
});