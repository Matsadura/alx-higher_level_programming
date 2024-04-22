#!/usr/bin/node

const { argv } = require('node:process');

const myInt = Number.parseInt(argv[2]);

if (isNaN(myInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myInt}`);
}
