#!/usr/bin/node
let argPrinted = 0;
exports.logMe = function (item) {
  console.log(`${argPrinted}: ${item}`);
  argPrinted++;
};
