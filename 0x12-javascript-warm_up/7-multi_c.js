#!/usr/bin/node
const x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; x > i; i++) {
    console.log('C is fun');
  }
}
