#!/usr/bin/node
const newSquare = require('./5-square');
class Square extends newSquare {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i <= this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.expots = Square;
