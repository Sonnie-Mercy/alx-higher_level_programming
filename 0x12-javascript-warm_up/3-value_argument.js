#!/usr/bin/node
const argtoprint = process.argv[2];

if (argtoprint === undefined) {
  console.log('No argument');
} else {
  console.log(argtoprint);
}
