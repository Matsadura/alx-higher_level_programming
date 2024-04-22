#!/usr/bin/node

const { argv } = require('node:process');
let firstLarge = 0;
let secondLarge = 0;

if (argv.length === 2 || argv.length === 3) {
  console.log('0');
} else {
  let counter;
  for (counter = 0; counter < argv.length; counter++) {
    if (argv[counter] > firstLarge) {
      firstLarge = argv[counter];
    }
  }
  for (counter = 0; counter < argv.length; counter++) {
    if ((argv[counter] > secondLarge) && argv[counter] !== firstLarge) {
      if (secondLarge < firstLarge) {
        secondLarge = argv[counter];
      }
    }
  }
  console.log(secondLarge);
}
