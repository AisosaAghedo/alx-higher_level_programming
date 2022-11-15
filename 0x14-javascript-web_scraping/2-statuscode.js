#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, res, data) {
  console.log('code:', res.statusCode);
  if (err) { console.log('code: ', err); }
});
