#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const swapi = 'https://swapi-api.alx-tools.com/api/films/:id' + movieID;
request.get(swapi, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
