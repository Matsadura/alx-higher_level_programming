#!/usr/bin/node

const { argv } = require('node:process');
let i;

if (typeof argv[2] === 'undefined') {
  console.log('Missing number of occurences');
} else if (argv[2] && argv[2] >= 1) {
  for (i = 0; i < argv[2]; i++) {
    console.log('C is fun');
  }
}
