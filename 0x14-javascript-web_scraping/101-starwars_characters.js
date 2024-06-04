#!/usr/bin/node

const movieId = process.argv.slice(2)[0];
const request = require('request');

if (movieId !== undefined) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
  request.get({ url, json: true }, (error, response, body) => {
    if (error) {
      console.log(error);
    }

    body.characters.forEach(characterUrl => {
      request.get({ url: characterUrl, json: true }, async (error, response, people) => {
        if (error) {
          console.log(error);
        }
        console.log(people.name);
      });
    });
  });
}
