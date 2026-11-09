"usestrict"

let numbers = [];

while (true) {

    let number = Number(prompt("Enter numbers, enter 0 to stop"));

    if (number === 0) {
        break;

    }

    numbers.push(number);
}

numbers.sort((a, b) => b - a);

console.log("numbers form largest to smallest ")

for (let i = 0; i < numbers.length; i++) {

    console.log(numbers [i]);
}