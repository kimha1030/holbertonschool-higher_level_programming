#!/usr/bin/node
// Task 7. I love C
const myArg1 = process.argv.slice(2);
const myNum = parseInt(myArg1[0]);
if (!myNum) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myNum; i++) {
    console.log('C is fun');
  }
}
