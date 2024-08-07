#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (!(w <= 0) && Number(w)) {
      if (!(h <= 0) && Number(h)) {
        this.width = w;
        this.height = h;
      }
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
