#!/usr/bin/node
const { argv } = require('process');

let num = parseInt(argv[2], 10);
if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
