#!/usr/bin/node
// Task 8. Right order

for (let x = 0; x < 10; x++) {
  const urlMovie = 'https://swapi-api.hbtn.io/api/people/?page=' + x;
  const idMovie = process.argv.slice(2, 3);
  const request = require('request');
  request(urlMovie, function (err, response, body) {
    if (err) {
      return console.log(err);
    }
    const results = JSON.parse(body).results;
    for (const i in results) {
      for (const j in results[i].films) {
        if (results[i].films[j].includes(idMovie[0])) {
          console.log(results[i].name);
        }
      }
    }
  });
}
