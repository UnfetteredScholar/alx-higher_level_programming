#!/usr/bin/node

const fs = require('node:fs');
const filename = process.argv[2];

fs.readFile(filename, 'utf8', (err, f) => {
  if (err) {
    return console.error(err);
  }
  console.log(f);
});
