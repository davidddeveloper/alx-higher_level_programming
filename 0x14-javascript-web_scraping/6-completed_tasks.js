#!/usr/bin/node

const request = require('request');

const argv = process.argv.slice(2);
const url = argv[0];

request.get({ url, json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const todosCompleted = { };

  body.forEach(todo => { todosCompleted[`${todo.userId}`] = 0; });

  body.forEach(todo => {
    if (todo.completed === true) {
      todosCompleted[`${todo.userId}`] += 1;
    }
  });
  console.log(todosCompleted);
});
