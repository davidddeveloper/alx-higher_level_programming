#!/usr/bin/node

const episodeId = process.argv.slice(2)[0];
const request = require('request');

if (episodeId !== undefined) {
  const url = `https://swapi-api.alx-tools.com/api/films/${episodeId}/`;
  request.get({ url, json: true }, (error, response, body) => {
    if (error) {
      console.log(error);
    }

    console.log(body.title);
  });
}
