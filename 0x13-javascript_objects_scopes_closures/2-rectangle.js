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
};
