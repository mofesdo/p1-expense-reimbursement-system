
function approved() {

    const formData = new FormData();

    formData.append("request_id",document.getElementById("row1button").value);

    fetch("/manager/approve",
    {
    method: 'POST'
    body: formData
    }
    );

}