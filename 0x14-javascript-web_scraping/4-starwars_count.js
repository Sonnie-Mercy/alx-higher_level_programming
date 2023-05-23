#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const results = JSON.parse(body).results;
    const count = results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0);

    console.log('Number of movies with Wedge Antilles:', count);
  } else {
    console.error('Unable to fetch movie data.');
  }
});
