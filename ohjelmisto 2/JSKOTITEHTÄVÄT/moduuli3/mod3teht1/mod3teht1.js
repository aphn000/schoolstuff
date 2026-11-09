"use strict"

let numbers = [];

for (let i = 0; i < 5; i++) {
    let number = Number(prompt("enter number " + (i + i) + ":"));
    numbers.push(number);

}

console.log("Numbersin reverse order: ")

for (let i = numbers.length - 1; i>= 0; i--) {

    console.log(numbers[i]);
}