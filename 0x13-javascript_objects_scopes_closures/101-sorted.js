#!/usr/bin/node

const dict = require('./101-data.js').dict;

let new_dict = {};
for (key of Object.keys(dict)) {
  if (new_dict[dict[key]]) {
    new_dict[dict[key]].push(key);
  }
  else {
    new_dict[dict[key]] = [key];
  }
}

console.log(new_dict);
