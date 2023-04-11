#!/usr/bin/node
const args = process.argv.slice(2);
const length = args.length;

if (length < 2) {
  console.log(0);
} else {
  const integers = args.map(Number);
  const arranged = integers.sort((a, b) => b - a);
  console.log(arranged[1]);
}
