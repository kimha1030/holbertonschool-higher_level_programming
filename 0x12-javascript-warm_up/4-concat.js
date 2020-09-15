#!/usr/bin/node
// Task 4. Create a sentence
const myArg1 = process.argv.slice(2, 3);
const myArg2 = process.argv.slice(3);
if (myArg1[0] && myArg2[0]) {
  console.log(myArg1[0] + ' is ' + myArg2[0]);
} else {
  console.log(myArg1[0] + ' is undefined');
}
