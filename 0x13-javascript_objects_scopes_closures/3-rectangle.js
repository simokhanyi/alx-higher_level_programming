#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      return {}; // Create an empty object if w or h is not a positive integer or either of them is 0
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (!this.width || !this.height) {
      console.log(''); // If the object is empty, print an empty line
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width)); // Print the rectangle using 'X' character
      }
    }
  }
}

module.exports = Rectangle;
