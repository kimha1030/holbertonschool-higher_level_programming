#!/usr/bin/node
// Task 0. Readme 
var nameFile = process.argv.slice(2, 3);
var fs = require('fs');
fs.readFile(nameFile[0], 'utf-8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
