#!/usr/bin/node
const request = require('request');
const character = 'https://swapi-api.hbtn.io/api/people/18/';
let count = 0;
request(process.argv[2], function (err, res, data) {
  if (err) {
    console.log(err);
  }
  data = JSON.parse(data).results;
  for (let i = 0; i < data.length; i++) {
    if (data[i].characters.includes(character)) {
      count++;
    }
  }
  console.log(count);
});
