#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (err, data) {
  console.log(data);
  if (err) {
    console.log(err);
  }
});
