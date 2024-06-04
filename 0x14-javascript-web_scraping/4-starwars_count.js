#!/usr/bin/node

const argv = process.argv;
const request = require('request');
const url = argv[2];
const charId = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const bodyJson = JSON.parse(body);
    let i = 0;
    for (const result of bodyJson.results) {
      if (result.characters.includes(charId)) {
        i++;
      }
    }
    console.log(i);
  }
});
