#!/usr/bin/node
// Task 10. Factorial
const myArg1 = process.argv.slice(2, 3);
const a = parseInt(myArg1[0]);
function factorial (a) {
  if (!a) {
    return ('1');
  } else {
    return a * factorial(a - 1);
  }
}
console.log(factorial(a));
