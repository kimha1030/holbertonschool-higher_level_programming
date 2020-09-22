#!/usr/bin/node
// Task 4. Star wars Wedge Antilles
const urlMovie = process.argv.slice(2, 3);
const request = require('request');
request(urlMovie[0], function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  const results = JSON.parse(body).results;
  let count = 0;
  for (const i in results) {
    for (const j in results[i].characters) {
      if (results[i].characters[j].includes('18')) { count = count + 1; }
    }
  }
  console.log(count);
});
