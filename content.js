console.log("✅ ReviewGuard content script loaded");

const reviews = document.querySelectorAll("[data-hook='review']");

reviews.forEach(async (reviewDiv) => {
  const reviewText = reviewDiv.innerText;

  try {
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ review: reviewText }),
    });

    const result = await response.json();

    // Create result badge
    const badge = document.createElement("div");
    badge.style.marginTop = "8px";
    badge.style.fontWeight = "bold";
    badge.style.fontSize = "14px";
    badge.style.color =
      result.prediction === "Suspicious" ? "orange" : "green";
    badge.textContent =
      result.prediction === "Suspicious" ? "⚠️ Suspicious" : "✅ Genuine";

    // Create explanation line
    const explanation = document.createElement("div");
    explanation.style.fontSize = "13px";
    explanation.style.color = "#555";
    explanation.style.marginTop = "3px";

    // Generate short explanation string
    if (result.prediction === "Suspicious") {
      if (result.flags?.length) {
        explanation.textContent = "🚩 " + result.flags.join(", ");
      } else {
        explanation.textContent = "This review has suspicious behavior patterns.";
      }
    } else {
      explanation.textContent = "Language and sentiment align well with verified status.";
    }

    // Append to review
    reviewDiv.appendChild(badge);
    reviewDiv.appendChild(explanation);
  } catch (error) {
    console.error("Error calling API:", error);
  }
});
