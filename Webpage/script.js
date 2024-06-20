document.getElementById('apiForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    var inputText = document.getElementById('inputText').value;
    
    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: inputText })
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('output').innerText = data;
    })
    .catch(error => {
        document.getElementById('output').innerText = "Parece haber un error, por favor inténtalo nuevamente";
        console.error('Error:', error);
    });
});
