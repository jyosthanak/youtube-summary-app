document.getElementById("summarizeBtn").addEventListener("click", async () => {
  const status = document.getElementById("status");
  const summaryBox = document.getElementById("summaryBox");
  status.innerText = "Fetching summary...";

  chrome.tabs.query({ active: true, currentWindow: true }, async (tabs) => {
    const url = tabs[0].url;
    try {
      const response = await fetch("http://127.0.0.1:5000/summarize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ youtube_url: url })
      });

      const data = await response.json();
      if (data.summary) {
        summaryBox.value = data.summary;
        status.innerText = "✅ Summary ready!";
      } else {
        summaryBox.value = "No summary returned.";
        status.innerText = "⚠️ Empty response.";
      }
    } catch (error) {
      summaryBox.value = "❌ Error fetching summary.";
      status.innerText = "❌ Check console for error.";
      console.error("SUMMARY ERROR:", error);
    }
  });
});
