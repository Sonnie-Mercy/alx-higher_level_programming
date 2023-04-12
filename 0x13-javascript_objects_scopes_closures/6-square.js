#!/usr/bin/node
const Squareone = require('./5-square');

module.exports = class Square extends Squareone {
  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    const row = c.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
};
