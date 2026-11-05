"use strict"

const name = prompt("What is name");

const number = Math.floor(Math.random() * 4) + 1;
let room;

switch(number) {

    case 1:
        room = "Gryffindor";
        break;

    case 2:
        room = "Slyhterin";
        break;

    case 3:
        room = "Hufflepuff";
        break;

    case 4:
        room = "Ravenclaw";
        break;


}

document.getElementById("result").textContent =
   `${name}, you are ${room}.`;