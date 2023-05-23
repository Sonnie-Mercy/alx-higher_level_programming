#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const charId = 18;

request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const movies = films.filter((film) =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${charId}/`)
    );

    console.log('Number of movies with Wedge Antilles:', movies.length);
  } else {
    console.error('Unable to fetch movie data.');
  }
});
