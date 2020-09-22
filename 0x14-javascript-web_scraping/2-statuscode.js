#!/usr/bin/node
// Task 2 - Status Code
const urlReq = process.argv.slice(2, 3);
const request = require('request');
request.get(urlReq[0], function (response, body) {
  console.log('code:', body.statusCode); // Print the HTML for the Google homepage.
});
