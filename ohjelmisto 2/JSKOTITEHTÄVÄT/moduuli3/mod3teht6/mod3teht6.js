"usestrict"

function rollDice () {

    return Math.floor(Math.random()* 6) + 1;

}

let list = document.getElementById("diceList");

let result;

do {

    result = rollDice();

    let listItem = document.createElement ("li");

    listItem.textContent = result;

    list.appendChild(listItem);

} while (result !== 6);