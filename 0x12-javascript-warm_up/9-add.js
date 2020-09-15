#!/usr/bin/node
// Task 9. Add
const myArg1 = process.argv.slice(2, 3);
const a = parseInt(myArg1[0]);
const myArg2 = process.argv.slice(3);
const b = parseInt(myArg2[0]);
function add (a, b) {
  if (a && b) {
    return (a + b);
  } else {
    return ('NaN');
  }
}
console.log(add(a, b));
