#!/usr/bin/node

exports.callMeMoby = function callMeMoby (n, func) {
  for (let i = 0; i < n; i++) {
    func();
  }
};
