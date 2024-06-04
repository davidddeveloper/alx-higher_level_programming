#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const argv = process.argv.slice(2);
const url = argv[0];
const filePath = argv[1];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
