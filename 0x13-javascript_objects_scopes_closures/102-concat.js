#!/usr/bin/node

const file1 = process.argv[1];
const file2 = process.argv[2];
const destFile = process.argv[3];
let content1 = '';
let content2 = '';
fs = require("fs");

fs.readFile(file1, "utf8", function (err, data) {
  content1 = data;
});

fs.readFile(file2, "utf8", function (err, data) {
  content2 = data;
});

const content = content1 + content2;

fs.writeFile(destFile, content, err => {});
