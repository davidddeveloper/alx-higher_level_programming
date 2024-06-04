#!/usr/bin/node

const argv = process.argv.slice(2);
const url = argv[0];
const request = require('request');

if (url !== undefined) {
  request.get(url)
    .on('response', (response) => {
      console.log(response.statusCode);
    });
}
