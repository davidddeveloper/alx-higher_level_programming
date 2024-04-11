#!/usr/bin/node

const argv = process.argv.slice(2);
let n = Number(argv[0]);

if (isNaN(n)) {
  console.log('Missing size');
} else {
  n = Number(n);
  for (let i = 0; i < n; i++) {
    let row = '';
    for (let j = 0; j < n; j++) {
      row += 'x';
    }
    console.log(row);
  }
}
