#!/usr/bin/node
const process = require('process');
const runtime = process.argv[2];
let j = 0;
if (runtime) {
  while (j < runtime) {
    console.log('C is fun');
    j++;
  }
} else {
  console.log('Missing number of occurrences');
}
