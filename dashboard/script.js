async function checkReview() {
  const review = document.getElementById("reviewInput").value;

  const res = await fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ review }),
  });

  const data = await res.json();

  // Display prediction label
  document.getElementById("output").innerText = `Prediction: ${data.prediction}`;

  // Display explanation if available
  if (data.explanation) {
    let explainHTML = "<ul>";
    data.explanation.forEach((item) => {
      const word = item.word;
      const score = item.score;
      const color = score > 0 ? "green" : "red";
      explainHTML += `<li style="color: ${color};">${word}: ${score.toFixed(3)}</li>`;
    });
    explainHTML += "</ul>";
    document.getElementById("lime-visuals").innerHTML = explainHTML;
  } else {
    document.getElementById("lime-visuals").innerText = "No explanation available.";
  }
}
