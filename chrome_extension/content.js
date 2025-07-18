function scanReviews() {
  const reviews = document.querySelectorAll('[data-hook="review-body"], .t-ZTKy'); // Amazon + Flipkart

  reviews.forEach(async (reviewDiv) => {
    const text = reviewDiv.innerText.trim();
    if (!text) return;

    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ review: text })
      });

      const result = await response.json();

      const tag = document.createElement("div");
      tag.innerText = `⚠️ ${result.prediction}`;
      tag.style.color = result.prediction === "Suspicious" ? "red" : "green";
      tag.style.fontWeight = "bold";
      tag.style.marginTop = "5px";
      reviewDiv.appendChild(tag);
    } catch (err) {
      console.error("Review scan error:", err);
    }
  });
}

window.addEventListener("load", () => {
  setTimeout(scanReviews, 3000); // wait for reviews to render
});
