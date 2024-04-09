class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // If width or height is not a positive number, set them to undefined
      this.width = undefined;
      this.height = undefined;
    }
  }

  print () {
    if (this.width !== undefined && this.height !== undefined) {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += 'X';
        }
        console.log(row);
      }
    } else {
      console.log('Invalid dimensions. Cannot print rectangle.');
    }
  }

  rotate () {
    if (this.width !== undefined && this.height !== undefined) {
      // Swap width and height
      const temp = this.width;
      this.width = this.height;
      this.height = temp;
    } else {
      console.log('Invalid dimensions. Cannot rotate rectangle.');
    }
  }

  double () {
    if (this.width !== undefined && this.height !== undefined) {
      // Double the width and height
      this.width *= 2;
      this.height *= 2;
    } else {
      console.log('Invalid dimensions. Cannot double rectangle.');
    }
  }
}

module.exports = Rectangle;
