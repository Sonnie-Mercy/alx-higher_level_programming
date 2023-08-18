#!/usr/bin/node
const dict = require('./101-data');
const byId = {};
for (const userId in dict) {
  const occurrences = dict[userId];
  if (!byId[occurrences]) {
    byId[occurrences] = [];
  }
  byId[occurrences].push(userId);
}
console.log(byId);
