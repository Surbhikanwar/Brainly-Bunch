document.getElementById("checkBtn").addEventListener("click", async () => {
  const review = document.getElementById("reviewInput").value;

  const res = await fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ review })
  });

  const data = await res.json();
  document.getElementById("result").innerText = `Prediction: ${data.prediction}`;
});
