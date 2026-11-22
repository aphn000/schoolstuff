"usestrict"

let answer = confirm (" Should i calculate squareroot?");

if (answer) {

    let number = Number(prompt("Enter number:"));

    if (number < 0) {
        document.getElementById("result").textContent =
        "the square root of negtive number is not defined";
    } else {
        let squareroot = Math.sqrt(number);

        document.getElementById("result").textContent =
        "The squareroot of " + number + " is" + squareroot;
    }
} else {
    document.getElementById("result").textContent =
        "The square root is not calculated.";
}


