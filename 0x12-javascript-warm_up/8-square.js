#!/usr/bin/node
const { argv } = require('process');

let num = parseInt(argv[2], 10);
if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      process.stdout.write('#');
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}

