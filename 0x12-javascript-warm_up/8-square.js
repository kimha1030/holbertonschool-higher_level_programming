#!/usr/bin/node
// Task 8. Square
const myArg1 = process.argv.slice(2);
const myNum = parseInt(myArg1[0]);
const pattern = 'X';
if (!myNum) {
  console.log('Missing size');
} else {
  for (let j = 0; j < myNum; j++) {
    console.log(pattern.repeat(myNum));
  }
}
