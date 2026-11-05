"use strict"

const first = parseInt(prompt("Enter first integer"), 10)
const second = parseInt(prompt("Enter second integer"), 10)
const third = parseInt(prompt("Enter third integer"), 10)

const sum = first + second + third;
const product = first * second * third;
const average = sum / 3;

document.getElementById("sum").textContent = `sum: ${sum}`;
document.getElementById("product").textContent = `product: ${product}`;
document.getElementById("average").textContent = `avrg: ${average}`;
