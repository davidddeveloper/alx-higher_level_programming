#!/usr/bin/env node

const argv = process.argv.slice(2);
let left_operand = Number(argv[1]);
let right_operand = Number(argv[0]);

function add(a, b)
{
        console.log(a + b);
}

add(left_operand, right_operand);
