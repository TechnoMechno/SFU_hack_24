let currentMessage;


function getReq() {
    const url = 'http://localhost:5000/get-message'
    fetch(url)
    .then(response => response.json())  
    .then(req => {
       console.log(req);
       currentMessage = req;
        console.log(document.getElementById("something").innerHTML = JSON.stringify(req));
    })
}

document.getElementById("buttonChoice1").addEventListener('click', () => {
    getReq();
    document.getElementById("something").innerHTML = "<img src="+currentMessage.avatar+" alt=image>";
    console.log(currentMessage.avatar)
})
