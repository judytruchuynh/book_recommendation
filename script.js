document.getElementById("userSimilarityForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var user1 = document.getElementById("user1").value;
    var user2 = document.getElementById("user2").value;
    var method = document.getElementById("method").value;
    var url = "https://your-api-endpoint.com/calculate-user-similarity?user1=" + user1 + "&user2=" + user2 + "&method=" + method;
    fetch(url)
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText = "Similarity: " + data.similarity;
        })
        .catch(error => console.error('Error:', error));
});