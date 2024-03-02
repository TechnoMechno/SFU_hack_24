let currentMessage;


function getReq() {
    const url = 'http://localhost:5000/get-message'
    fetch(url)
    .then(response => response.json())  
    .then(req => {
       console.log(req);
       currentMessage = req;
        document.getElementById("something").innerHTML = JSON.stringify(req);
    })
}

document.getElementById("weird").addEventListener('click', () => {
    getReq();
    document.getElementById("something").src = currentMessage.avatar;
})
