#!/usr/bin/node
const fs = require('fs');
if (process.argv.length !== 5) {
  process.exit(1);
}
const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const File3 = process.argv[4];
try {
  const content1 = fs.readFileSync(sourceFile1, 'utf8');
  const content2 = fs.readFileSync(sourceFile2, 'utf8');
  const concatenated = content1 + content2;
  fs.writeFileSync(File3, concatenated, 'utf8');
  console.log(`Contents of ${sourceFile1} and ${sourceFile2} have been concatenated to ${File3}`);
} catch (error) {
  console.error('An error occurred:', error.message);
  process.exit(1);
}
