#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

const fetchMovieCharacters = (movieId) => {
  const movieUrl = `${apiUrl}${movieId}`;

  request(movieUrl, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const characters = JSON.parse(body).characters;

      characters.forEach((characterUrl) => {
        request(characterUrl, function (error, response, body) {
          if (!error && response.statusCode === 200) {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
          }
        });
      });
    }
  });
};

fetchMovieCharacters(movieId);
