#!/usr/bin/node
const Square = require('./5-square');
class newSquare extends Square {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i <= this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}
module.exports = newSquare;
