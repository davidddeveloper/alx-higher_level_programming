#!/usr/bin/node

const dict = require('./101-data.js').dict;

const newDict = {};
for (const key of Object.keys(dict)) {
  if (newDict[dict[key]]) {
    newDict[dict[key]].push(key);}
  else {
    newDict[dict[key]] = [key];
  }
}

console.log(newDict);
