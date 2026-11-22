"usestrict"

function even(numbers) {

    let evenNumbers = [];

        for (let i = 0; i < numbers.length; i++) {
            if (numbers[i] % 2 === 0) {
            evenNumbers.push(numbers[i]);
        }
    }

return evenNumbers;

}

let originalArray = [2,7,4,14,11,25,22];

let newArray = even(originalArray);

console.log("Original array ", originalArray);

console.log("Even numbers ", newArray);