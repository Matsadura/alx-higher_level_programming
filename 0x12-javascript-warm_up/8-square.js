#!/usr/bin/node

const { argv } = require('node:process');
const size = Number.parseInt(argv[2]);

let i;

if (isNaN(size)) {
  console.log('Missing Size');
} else {
  for (i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
