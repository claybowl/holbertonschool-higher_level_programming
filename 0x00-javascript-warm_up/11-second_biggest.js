#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const array = process.argv.slice(2).sort((a, b) => a - b);
  console.log(array[array.length - 2]);
}
