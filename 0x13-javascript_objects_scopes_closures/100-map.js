#!/usr/bin/node

const data = require('./100-data.js').list;
console.log(data);

let = data.map(function (val, idx) {
  return (val * idx);
});
console.log(new_data);
