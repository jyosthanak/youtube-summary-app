document.getElementById("summarizeBtn").addEventListener("click", async () => {
  const status = document.getElementById("status");
  const summaryBox = document.getElementById("summaryBox");
  status.style.display = "block";
  status.innerText = "Fetching summary...";
  status.style.color = "#374151"; // Neutral gray

  chrome.tabs.query({ active: true, currentWindow: true }, async (tabs) => {
    const url = tabs[0].url;
    try {
      const response = await fetch("http://localhost:5000/summarize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ youtube_url: url })
      });

      const data = await response.json();
      if (data.summary) {
        summaryBox.value = data.summary;
        status.innerText = "✅ Summary ready!";
        status.style.color = "#16a34a"; // Green
      } else {
        summaryBox.value = "No summary returned.";
        status.innerText = "⚠️ Empty response.";
        status.style.color = "#f59e0b"; // Yellow
      }
    } catch (error) {
      summaryBox.value = "❌ Error fetching summary.";
      status.innerText = "❌ Check console for error.";
      status.style.color = "#dc2626"; // Red
      console.error("SUMMARY ERROR:", error);
    }
  });
});
