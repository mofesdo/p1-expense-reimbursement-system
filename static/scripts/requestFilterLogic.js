var radioOngoing = document.getElementById("status0");
var radioApproved = document.getElementById("status1");
var radioDenied = document.getElementById("status2");
var radioCanceled = document.getElementById("status3");
var radioNormal = document.getElementById("urgent0");
var radioUrgent = document.getElementById("urgent1");


function ongoing() {
    var stuff = document.getElementsByClassName("ongoing");
    
    for (const element of stuff) {
        if (element.style.display == 'none') {
            element.style.display = 'block';
        } else {
            element.style.display = 'none';
        }
    }
}

function approved() {
    var stuff = document.getElementsByClassName("approved");

    for (const element of stuff) {
        if (element.style.display == 'none') {
            element.style.display = 'block';
        } else {
            element.style.display = 'none';
        }
    }
}

function denied() {
    var stuff = document.getElementsByClassName("denied");

    for (const element of stuff) {
        if (element.style.display == 'none') {
            element.style.display = 'block';
        } else {
            element.style.display = 'none';
        }
    }
}

function canceled() {
    var stuff = document.getElementsByClassName("canceled");

    for (const element of stuff) {
        if (element.style.display == 'none') {
            element.style.display = 'block';
        } else {
            element.style.display = 'none';
        }
    }
}

function normal() {
    var stuff = document.getElementsByClassName("normal");

    for (const element of stuff) {
        if (element.style.display == 'none') {
            element.style.display = 'block';
        } else {
            element.style.display = 'none';
        }
    }
}

function urgent() {
    var stuff = document.getElementsByClassName("urgent");

    for (const element of stuff) {
        if (element.style.display == 'none') {
            element.style.display = 'block';
        } else {
            element.style.display = 'none';
        }
    }
}


radioOngoing.addEventListener("click",ongoing);
radioApproved.addEventListener("click",approved);
radioDenied.addEventListener("click",denied);
radioCanceled.addEventListener("click",canceled);
radioNormal.addEventListener("click",normal);
radioUrgent.addEventListener("click",urgent);