
let currentData = "";
let lastData = "";

fetch('/chatroom-messages/19')
    .then(response => response.json())
    .then(data => {
        lastData = JSON.stringify(data);
    })
    .catch(error => console.error('There was an error during initial fetch!', error));

function updateTexts() {
    fetch('/chatroom-messages/19')
        .then(response => response.json())
        .then(data => {
            currentData = JSON.stringify(data);
            if (currentData !== lastData) {
                console.log('Data Changed');
                lastData = currentData; // Update lastData to the current data after change is detected
            }
        })
        .catch(error => console.error('There was an error during update fetch!', error));
}

setInterval(updateTexts, 1000);
