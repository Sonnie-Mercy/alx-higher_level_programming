#!/usr/bin/node

const request = require('request');
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request.get(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    console.log('Title:', movieData.title);
  } else {
    console.error('Unable to fetch movie data.');
  }
});
