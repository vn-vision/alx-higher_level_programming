#!/usr/bin/node
// class Square extends from Rectangle 4
// takes one argument in constructor
// @size: size of the square

// import the class from the file
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  // class Square inherits Rectangle

  constructor (size) {
    // constructor for square
    super(size, size);
  }
}

module.exports = Square;
