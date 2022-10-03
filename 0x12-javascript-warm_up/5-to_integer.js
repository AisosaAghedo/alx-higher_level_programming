#!/usr/bin/node
const process = require('process');
const number = parseInt(process.argv[2]);
if (process.argv.length < 3) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
