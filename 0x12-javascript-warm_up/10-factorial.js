#!/usr/bin/node

const argv = process.argv.slice(2);

function factorial (n) {
  if (n === 0) {
    return;
  };
  return (factorial(n--));
};

console.log(factorial(argv[0]));
