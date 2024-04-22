#!/usr/bin/node

const factStart = process.argv[2];

function facto (arg) {
  if (arg === 0) {
    return (1);
  }
  if (arg === 1) {
    return (1);
  }
  if (isNaN(arg) || arg === undefined) {
    return (1);
  }

  return (arg * facto(arg - 1));
}

console.log(facto(factStart));
