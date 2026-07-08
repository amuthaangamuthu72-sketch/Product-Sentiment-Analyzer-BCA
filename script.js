document.getElementById("submitBtn").addEventListener("click", function () {

    fetch("http://127.0.0.1:5000/products", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            product_name: document.getElementById("product").value,
            review: document.getElementById("review").value,
            polarity: 0.85,
            sentiment: "Positive"
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        alert("Error: " + error);
        console.error(error);
    });

});