'use strict';

const linkit = document.querySelectorAll('a');

linkit.forEach(function(linkki) {
  if (linkki.textContent.trim() === 'Koira') {
    linkki.href = 'https://fi.wikipedia.org/wiki/Koira';
  }
});


const ol = document.querySelector('ol');
const kissalisays = document.createElement('li');
kissalisays.innerText = 'Kissat pärjäävät mainiosti yksinäänkin.';
ol.appendChild(kissalisays);

const ul = document.querySelector('ul')(0);
const koiralisays = document.createElement('li');
koiralisays.innerText = 'Monet koirat palvovat omistajaansa.';
ul.appendChild(koiralisays);


const button = document.querySelector('button');

button.addEventListener('click', function(evt) {
  alert('Elementtiä ' + evt.currentTarget.tagName + ' klikattiin');
});

window.addEventListener('keydown', function(evt) {
  console.log(evt.key);

  if (evt.key === 'k') {
    alert('Painoit salaista nappia!');
  }
});