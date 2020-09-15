#!/usr/bin/node
// Task 5. An Integer
const myArg1 = process.argv.slice(2);
const myNum = parseInt(myArg1[0]);
if (!myNum) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myNum);
}
