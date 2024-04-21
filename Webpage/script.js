document.getElementById('apiForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    var inputText = document.getElementById('inputText').value;
    
    fetch('https://mkarmelic.pythonanywhere.com/api/endpoint', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: inputText })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('output').innerText = data.prediction;
    })
    .catch(error => {
        document.getElementById('output').innerText = "Parece haber un error, por favor inténtalo nuevamente";
        console.error('Error:', error);
    });
});
