#!/usr/bin/node

const data = require('./100-data.js').list;
console.log(data);

const newData = data.map(function (val, idx) {
  return (val * idx);
});
console.log(newData);
