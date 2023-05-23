#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  if (index >= characters.length) {
    return;
  }

  const characterUrl = characters[index];
  request(characterUrl, function (error, response, body) {
    if (!error) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    }

    printCharacters(characters, index + 1);
  });
}
