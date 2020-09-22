#!/usr/bin/node
// Task 6. How many completed?
const urlTask = process.argv.slice(2, 3);
const request = require('request');
request(urlTask[0], function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  const results = JSON.parse(body);
  const newObj = {};
  for (const i in results) {
    if (results[i].completed === true) {
      const idUser = results[i].userId;
      if (newObj[idUser]) {
        newObj[idUser] = newObj[idUser] + 1;
      } else {
        newObj[idUser] = 1;
      }
    }
  }
  console.log(newObj);
});
