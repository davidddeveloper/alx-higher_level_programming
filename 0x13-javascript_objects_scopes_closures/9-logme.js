#!/usr/bin/node

number_of_args = -1;
exports.logMe = function (item) {
  number_of_args += 1;
  console.log(number_of_args, item);
}
