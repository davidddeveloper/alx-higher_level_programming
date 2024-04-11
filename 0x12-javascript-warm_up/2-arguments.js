#!/usr/bin/node

const lengthOfArgv = process.argv.length;
let result;
if (lengthOfArgv < 3) {
  result = 'No argument';
} else if (lengthOfArgv === 3) {
  result = 'Argument found';
} else {
  result = 'Arguments found';
}
console.log(result);
