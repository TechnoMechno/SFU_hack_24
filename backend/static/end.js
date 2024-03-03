let currentMessage;

function getReq() {
    let userInput = document.getElementById("user_input").value;

    let url = "/process-input/"+userInput;
    return fetch(url)
        .then(req => req.json())
        .then(data => {
            currentMessage = data; // Convert JSON data to a string
            console.log(currentMessage);
            return currentMessage; // Return the JSON string
        });
}


document.getElementById("input").addEventListener("click", () => {
        getReq().then((currentMessage) => {
            let currentMessageData = currentMessage;
            document.getElementById("question-box").innerText = currentMessageData[0];
            document.getElementById("something").innerHTML = "<img src="+currentMessageData[1]+" alt=image>";
            console.log(currentMessageData[1]);
        }).catch(error => {
            console.error('Error fetching data:', error);
        });
    });
