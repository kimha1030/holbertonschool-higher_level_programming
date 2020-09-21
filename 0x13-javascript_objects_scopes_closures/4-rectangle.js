#!/usr/bin/node
// Task 4. Rectangle #4
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Methods of instance
  print () {
    const myWidth = parseInt(this.width);
    const myHeight = parseInt(this.height);
    const pattern = 'X';
    for (let j = 0; j < myHeight; j++) {
      console.log(pattern.repeat(myWidth));
    }
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }
}

module.exports = Rectangle;
