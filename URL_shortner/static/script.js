async function shortenUrl() {
    const originalUrl = document.getElementById("originalUrl").value;
    const resultDiv = document.getElementById("result");

    if (!originalUrl) {
        resultDiv.innerText = "Please enter a URL!";
        return;
    }

    try {
        const response = await fetch("/shorten", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ original_url: originalUrl })
        });

        if (!response.ok) {
            resultDiv.innerText = "Error shortening URL!";
            return;
        }

        const data = await response.json();
        const shortUrl = `${window.location.origin}/${data.short_code}`;
        resultDiv.innerHTML = `Short URL: <a href="${shortUrl}" target="_blank">${shortUrl}</a>`;
    } catch (error) {
        resultDiv.innerText = "Network error!";
        console.error(error);
    }
}