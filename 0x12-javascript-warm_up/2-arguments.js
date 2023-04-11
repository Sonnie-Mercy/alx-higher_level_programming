#!/usr/bin/node
const args = process.argv.slice(2);
const theArgs = args.length;

if (theArgs === 0) {
  console.log('No argument');
} else if (theArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
