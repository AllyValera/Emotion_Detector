function RunSentimentAnalysis() {
    const text = document.getElementById("textToAnalyze").value;

    fetch("/emotionDetector", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text_to_analyze: text })
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById("system_response").innerHTML = data;
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("system_response").innerHTML = "Error occurred.";
    });
}