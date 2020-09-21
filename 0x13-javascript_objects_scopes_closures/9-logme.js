#!/usr/bin/node
// Task 9. Log me
var count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
