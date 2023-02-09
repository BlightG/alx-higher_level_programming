#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process');

fs.readFile(argv[2], 'utf8', (err, inputD) => {
  if (err) throw err;
  console.log(inputD.toString());
});
