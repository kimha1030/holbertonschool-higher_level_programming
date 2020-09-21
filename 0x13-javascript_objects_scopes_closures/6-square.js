#!/usr/bin/node
// Task 6. Square #1

const parSquare = require('./5-square');

class Square extends parSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      const pattern = c;
      for (let j = 0; j < this.width; j++) {
        console.log(pattern.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
