'use strict';
const names = ['John', 'Paul', 'Jones'];

let html = '<ul>';

for (let i = 0; i < names.length; i++) {
    html += `<li>${names[i]}</li>`;
}
html += '</ul>'

document.getElementById("target").innerHTML = html;