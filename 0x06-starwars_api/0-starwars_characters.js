#!/home/jeff/.nvm/versions/node/v21.6.2/bin/node

const request = require('request');

const filmId = process.argv[2];
const filmsUrl = 'https://swapi-api.alx-tools.com/api/films';
const url = `${filmsUrl}/${filmId}/`;
const charactersArray = [];

function addOne (value) {
  charactersArray.push(value);
}

request(url, (error, response, body) => {
  if (error) ;
  const characterUrls = JSON.parse(body).characters;
  characterUrls.forEach((elem) => {
    request(elem, (error, response, body) => {
      if (error) ;
      const json = JSON.parse(body);
      addOne({ name: json.name, created: new Date(json.created) });
    });
  });
});

setTimeout(() => {
  charactersArray.sort((a, b) => a.created - b.created);
  charactersArray.forEach((elem) => console.log(elem.name));
}, 5000);
