#!/usr/bin/node

const argv = process.argv.slice(2);
const leftOperand = Number(argv[1]);
const rightOperand = Number(argv[0]);

function add (a, b) {
  console.log(a + b);
}

add(leftOperand, rightOperand);
