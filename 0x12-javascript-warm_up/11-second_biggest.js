#!/usr/bin/node
const process = require('process');
let secondLargest = 0;
const number = process.argv.slice(2);
if (!number) {
	console.log(0);
} if (number === 1){
	console.log(0);
} else {
  number.sort();
  secondLargest = number[number.length - 2];
}
console.log(secondLargest);
