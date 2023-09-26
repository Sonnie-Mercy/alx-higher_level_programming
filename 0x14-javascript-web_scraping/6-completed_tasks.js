#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error == null) {
    const json = JSON.parse(body);
    for (let i = 0; i < json.length; i++) {
      if (json[i].completed === true) {
        if (response[json[i].userId] === undefined) {
          response[json[i].userId] = 0;
        }
        response[json[i].userId]++;
      }
    }
    console.log(response);
  }
});
