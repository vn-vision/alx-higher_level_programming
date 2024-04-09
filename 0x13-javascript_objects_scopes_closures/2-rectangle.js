#!/usr/bin/node
// Define class Rectangle that defines a rectangle
// Rectangle - class
// @w: width
// @h: height
// if height or width <= 0 , create empty object

class Rectangle {

  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
