#!/usr/bin/node
// Task 6. Square #1

const parSquare = require('./5-square');

class Square extends parSquare {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c) {
      const myWidth = parseInt(this.size);
      const myHeight = parseInt(this.size);
      const pattern = c;
      for (let j = 0; j < myHeight; j++) {
        console.log(pattern.repeat(myWidth));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
