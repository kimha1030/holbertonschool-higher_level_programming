#!/usr/bin/node
// Task 5. Loripsum
const urlReq = process.argv.slice(2, 3);
const nameFile = process.argv.slice(3);
const request = require('request');
const fs = require('fs');
request(urlReq[0], function (req, res, body) {
  fs.writeFile(nameFile[0], body, 'utf-8', function (err, data) {
    if (err) {
      return console.log(err);
    }
  });
});
