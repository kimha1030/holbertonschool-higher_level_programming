#!/usr/bin/node
// Task 9. Log me
let count = 0;
exports.logMe = function (item) {
  console.log('%d: %s', count, item);
  count = count + 1;
};
