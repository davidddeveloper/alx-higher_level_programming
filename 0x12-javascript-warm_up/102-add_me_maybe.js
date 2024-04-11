#!/usr/bin/node

exports.addMeMaybe = function addMeMaybe (n, func) {
  n++;
  func(n);
};
