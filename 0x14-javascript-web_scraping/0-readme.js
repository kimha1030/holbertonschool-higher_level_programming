#!/usr/bin/node
// Task 0. Readme
const nameFile = process.argv.slice(2, 3);
const fs = require('fs');
fs.readFile(nameFile[0], 'utf-8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
