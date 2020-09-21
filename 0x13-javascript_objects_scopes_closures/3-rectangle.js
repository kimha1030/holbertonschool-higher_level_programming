#!/usr/bin/node
// Task 3. Rectangle #3
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Method of instance
  print () {
    const myWidth = parseInt(this.width);
    const myHeight = parseInt(this.height);
    const pattern = 'X';
    for (let j = 0; j < myHeight; j++) {
      console.log(pattern.repeat(myWidth));
    }
  }
}

module.exports = Rectangle;
