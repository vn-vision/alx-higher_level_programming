#!/usr/bin/node

const Squa = require('./5-square.js');
class Square extends Squa {
  charPrint (C) {
    if (C) {
      for (let i = 0; i < this.height; i++) {
        console.log(C.repeat(this.width));
      }
    } else { this.print(); }
  }
}

module.exports = Square;
