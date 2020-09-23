#!/usr/bin/node
// Task 7. Who was playing in this movie?
const idMovie = process.argv.slice(2, 3);
const urlMovie = 'https://swapi-api.hbtn.io/api/films/' + idMovie[0];
const request = require('request');
request(urlMovie, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  const results = JSON.parse(body).characters;
  for (const i in results) {
    request(results[i], function (err, response, body) {
      if (err) {
        return console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
