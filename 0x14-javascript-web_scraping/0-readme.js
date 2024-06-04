#!/usr/bin/node

const fs = require('fs');
const argv = process.argv.slice(2);
const filePath = argv[0];

if (filePath !== undefined) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) { console.log(err); } else { console.log(data); }
  });
}
