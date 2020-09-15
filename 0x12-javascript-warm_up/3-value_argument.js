#!/usr/bin/node
// Task 3. Value of my argument
const myVar = process.argv.slice(2);
if (myVar == '') {
  console.log('No argument');
} else {
  console.log(myVar[0]);
}
