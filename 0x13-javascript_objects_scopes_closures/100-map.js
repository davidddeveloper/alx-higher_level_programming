#!/usr/bin/node

data = require('./100-data.js').list;
console.log(data);

new_data = data.map(function (val, idx) {
  return (val * idx);
});
console.log(new_data);
