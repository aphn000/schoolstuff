"use strict"


let numbers = [];

while (true) {

    let number = Number(prompt("Enter different numbers, stop at dupliacate number"));

    if (numbers.includes(number)) {
        alert("number has already been given");
        break;

    }

    numbers.push(number);
}

numbers.sort((a, b) => a - b);

console.log("numbers in ascending order ");

for (let i = 0; i < numbers.length; i++) {

    console.log(numbers [i]);
}