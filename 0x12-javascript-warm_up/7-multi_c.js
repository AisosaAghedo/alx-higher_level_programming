#!/usr/bin/node
const process = require('process');
const number = parseInt(process.argv[2]);
if (!number) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
