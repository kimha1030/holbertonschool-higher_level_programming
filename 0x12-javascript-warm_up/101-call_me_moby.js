#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let times;
  for (times = 0; times < x; times++) {
    theFunction();
  }
};
