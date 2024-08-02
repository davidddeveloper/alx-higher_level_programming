#!/usr/bin/node

const Square = require('./5-square.js');

module.exports = class Square extends Square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let chr = "X";
    if (c) {
      chr = c;
    }

    for (let i = 0; i < this.size; i++) {
      let row = '';
      for (let j = 0; j < this.size; j++) {
        row += chr;
      }
      console.log(row);
    }
  }
};
