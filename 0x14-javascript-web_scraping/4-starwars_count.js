#!/usr/bin/node

const argv = process.argv;
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const charId = 'https://swapi-api.alx-tools.com/api/people/' + argv[2] + '/';

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
