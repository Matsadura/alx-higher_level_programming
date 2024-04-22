#!/usr/bin/node

const { argv } = require('node:process');
const size = Number.parseInt(argv[2]);

let i, j;

if (isNaN(size)) {
  console.log('Missing Size');
} else {
  for (i = 0; i < size; i++) {
    let mySquare = '';

    for (j = 0; j < size; j++) {
      mySquare += 'X';
    }
    console.log(mySquare);
  }
}
