#!/usr/bin/node
const process = require('process');
const number = parseInt(process.argv[2]);
function factorial (number) {
  if (!number || number === 1) {
    return (1);
  } else {
    return (number * factorial(number - 1));
  }
}
console.log(factorial(number));
