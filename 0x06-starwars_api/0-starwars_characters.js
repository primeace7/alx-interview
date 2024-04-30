#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const filmsUrl = 'https://swapi-api.alx-tools.com/api/films';
const url = `${filmsUrl}/${filmId}/`;

request(url, (error, response, body) => {
  const characters = JSON.parse(body).characters;
  if (error) ;
  characters.map(function (elem) {
    request(elem, function (error, response, body) {
      if (error) ;
      console.log(JSON.parse(body).name);
    });
    return null;
  });
});
