#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, res, data) {
  console.log(JSON.parse(data).title);
  if (err) { console.log(err); }
});
