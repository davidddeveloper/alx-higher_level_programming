#!/usr/bin/node

const url = process.argv.slice(2)[0];
const request = require('request');

if (url !== undefined) {
  request.get({ url, json: true }, (error, response, body) => {
    if (error) {
      console.log(error);
    }

    const films = body;
    let numberOfFilm = 0;
    const characterApi = 'https://swapi-api.alx-tools.com/api/people/18/';

    for (const film of films.results) {
      film.characters.forEach(character => {
        if (characterApi === character) { numberOfFilm += 1; }
      });
    }

    console.log(numberOfFilm);
  });
}
