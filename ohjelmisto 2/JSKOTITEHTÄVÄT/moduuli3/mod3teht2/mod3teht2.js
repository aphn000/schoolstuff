"use strict"

let numberOfParticipants = Number(prompt("Enter number of participants"));

for (let i = 0; i < numberOfParticipants; i++) {
    let name = prompt("Enter participant " + (i + 1) + " name");
    participants.push(name);
}

participants.sort();

let list = document.getElementById("participantList");

for (let i = 0; i < participants.length; i++) {
    let listItem = document.createElement("li");
    listItem.textContent = participants[i];
    list.appendChild(listItem);
}