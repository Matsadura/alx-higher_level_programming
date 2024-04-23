#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {
  1: [],
  2: [],
  3: []
};

for (const [key, value] of Object.entries(dict)) {
  newDict[value].push(key);
}
console.log(newDict);
