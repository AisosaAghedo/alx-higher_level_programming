#!/usr/bin/node
const process = require('process');
let secondLargest = 0;
const number = parseInt(process.argv.slice(2));
if (number.length > 1) {
  number.sort();
  secondLargest = number[number.length - 2];
}
console.log(secondLargest);
