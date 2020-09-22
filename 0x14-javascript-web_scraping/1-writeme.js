#!/usr/bin/node
// Task 1. Write me
const nameFile = process.argv.slice(2, 3);
const strWrite = process.argv.slice(3);
const fs = require('fs');
fs.writeFile(nameFile[0], strWrite, 'utf-8', function (err, data) {
  if (err) {
    return console.log(err);
  }
});
