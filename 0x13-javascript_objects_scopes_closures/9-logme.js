#!/usr/bin/node

let numberOfArgs = -1;
exports.logMe = function (item) {
  numberOfArgs += 1;
  console.log(numberOfArgs, item);
};
