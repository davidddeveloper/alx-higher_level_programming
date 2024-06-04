#!/usr/bin/node

const fs = require('fs');
const argv = process.argv.slice(2);
const filePath = argv[0];
const data = argv[1];

if (filePath !== undefined && data !== undefined) {
  fs.writeFile(filePath, data, 'utf-8', (err) => {
    if (err) { console.log(err); }
  });
}
