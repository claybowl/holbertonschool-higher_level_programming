#!/usr/bin/node
const fs = require('fs');
const fileName = process.argv.slice(2);
fs.readFile(fileName[0], 'utf8', (err, data) => {
  if (err) throw err;

  console.log(data);
});
