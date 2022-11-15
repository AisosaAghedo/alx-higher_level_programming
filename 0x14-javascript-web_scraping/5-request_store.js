#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request(process.argv[2], function (err, res, data) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(process.argv[3], data, 'utf8', function (err, data) {
    if (err) {
      console.log(err);
    }
  });
});
