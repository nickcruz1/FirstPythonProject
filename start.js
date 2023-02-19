// Pull Python File Into index.html file Using JavaScript

function pullPython() {


let file = "start.py";


fetch (file)
.then(x => x.text())
.then(y => document.getElementById("demo").innerHTML = y);

   
    

}


function deletePython() {
let demo = document.getElementById("demo")


demo.innerHTML = "";

}


