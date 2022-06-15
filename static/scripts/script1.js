//for (let i = 0; i < document.getElementById("hidden_rowcount").value; i++) {
//    document.getElementById("button{{request[0]}}".addEventListener("click", approved("{{request[0]}}")))
//}

function sort_asc() {
window.location.replace(window.location.href.split('?')[0]+'?sortmode=asc');
}

function sort_desc() {
window.location.replace(window.location.href.split('?')[0]+'?sortmode=desc');
}


function approval(num) {

    const formData = new FormData();
    var response;

    formData.append("request_id",num);

    fetch("/manager/approve",
    {
    method: 'POST',
    body: formData
    }
    )
    .then(r => response = r);

    window.location.reload()
}


function declined(num) {

    const formData = new FormData();
    var response;

    formData.append("request_id",num);

    fetch("/manager/decline",
    {
    method: 'POST',
    body: formData
    }
    )
    .then(r => response = r);

    window.location.reload()
}

//<button id="btn">Click me!</button>
//
//var btn = document.getElementById("btn");
//btn.addEventListener("click", function() {
//	//Do something here
//}, false);