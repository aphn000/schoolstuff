"usestrict"
let dogs = [];

for (let i = 0; i < 6; i++) {
    let name = prompt ("Enter dog " + (i + 1) + "name");
    dogs.push(name);
}

dogs.sort();
dogs.reverse();

let list = document.getElementById("dogList");

for (let i = 0; i < dogs.length; i++) {
    let listItem = document.createElement ("li");
    listItem.textContent = dogs[i];
    list.appendChild(listItem);

}