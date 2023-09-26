#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, (error, response) => {
	console.log(error || `code: ${response.statusCode}`);
});
