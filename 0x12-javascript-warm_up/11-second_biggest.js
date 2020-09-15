#!/usr/bin/node
// Task 11. Second biggest!
const myVar = process.argv;
if (myVar.length === 2 || myVar.length === 3) {
  console.log('0');
} else {
  const myArg = process.argv.slice(2);
  const intArray = [];
  for (let i = 0; i < myArg.length; i++) {
    intArray[i] = parseInt(myArg[i]);
  }
  const myNums = intArray.sort(compareNumbers);
  const newLenght = myNums.length;
  console.log(myNums[newLenght - 2]);
}

function compareNumbers (a, b) {
  return a - b;
}
