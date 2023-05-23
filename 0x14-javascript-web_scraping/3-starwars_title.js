#!/usr/bin/node

const request = require('request');
const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
