#!/usr/bin/node
// Class Rectangle that takes height and width
// if w or h is equal to 0 or less return create empty
// print - prints the rectangle

class Rectangle {
  width;
  height;
  row;

  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      this.row = '';
      for (let j = 0; j < this.width; j++) {
        this.row += 'X';
      }
      console.log(this.row);
    }
  }
}

module.exports = Rectangle;
