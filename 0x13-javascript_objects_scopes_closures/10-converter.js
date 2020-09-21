#!/usr/bin/node
// Task 10. Number conversion
exports.converter = function (base) {
  return function (numConvert) {
    return numConvert.toString(base);
  };
};
