var checkOngoing = document.getElementById("status0");
var checkApproved = document.getElementById("status1");
var checkDenied = document.getElementById("status2");
var checkCanceled = document.getElementById("status3");
var checkNormal = document.getElementById("urgent0");
var checkUrgent = document.getElementById("urgent1");


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


checkOngoing.addEventListener("click",ongoing);
checkApproved.addEventListener("click",approved);
checkDenied.addEventListener("click",denied);
checkCanceled.addEventListener("click",canceled);
checkNormal.addEventListener("click",normal);
checkUrgent.addEventListener("click",urgent);