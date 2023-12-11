

function submitForm(event) {
    var age = document.getElementById("age").value;
    var sex = document.getElementById("sex").value;
    var bmi = document.getElementById("bmi").value;
    var children = document.getElementById("children").value;
    var smoker = document.getElementById("smoker").value;
    var region = document.getElementById("region").value;

    // Send data to the backend
    fetch("/process", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ age: age, sex: sex, bmi: bmi, children: children,smoker: smoker, region: region })
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the backend
        console.log(data);
    })
    .catch(error => {
        console.error("Error:", error);
    });

    submitFormData();
}

function submitFormData() {
    // Get form data
    const formData = new FormData(document.getElementById('insuranceForm'));

    // Make an asynchronous request to the server
    fetch('/submit', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        // Update the result section with the prediction
        document.getElementById('predictionResult').innerText = data;
        // Show the result section
        document.getElementById('resultSection').style.display = 'block';
    })
    .catch(error => console.error('Error:', error));
}
