#!/usr/bin/node
const process = require('process');
let args = process.argv.slice(2);
let n = args.length;
if (n === 0) {
  console.log('No argument');
  } else if (n === 1) {
      console.log('Arguments found');
    } else {
    console.log('Arguments found');
}
