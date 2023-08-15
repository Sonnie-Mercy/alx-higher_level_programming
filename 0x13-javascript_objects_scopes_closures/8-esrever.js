#!/usr/bin/node
exports.esrever = function (list) {
  const reverser = [];
  for (let i = 0; i < list.length; i++) {
    reverser.unshift(list[i]);
  }
  return reverser;
};
