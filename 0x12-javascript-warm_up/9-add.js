#!/usr/bin/node
function add (a, b) {
  console.log(parseInt(a)+ parseInt(b));
}
console.log(add(process.argv[2], process.argv[3]));
