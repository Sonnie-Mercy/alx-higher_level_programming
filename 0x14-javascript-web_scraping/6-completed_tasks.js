#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    const resp = {};
    const todos = JSON.parse(body);
    todos.forEach(function(todo) {
      if (todo.completed) {
        if (resp[todo.userId] === undefined) {
          resp[todo.userId] = 0;
        }
        resp[todo.userId]++;
      }
    });
    console.log(resp);
  }
});
