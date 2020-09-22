#!/usr/bin/node
// Task 3. Star wars movie title
const idMovie = process.argv.slice(2, 3);
const urlMovie = 'https://swapi-api.hbtn.io/api/films/' + idMovie[0];
const request = require('request');
request(urlMovie, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
