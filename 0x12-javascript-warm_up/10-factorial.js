#!/usr/bin/node
const { argv } = require('process');

let num = parseInt(argv[2], 10);

function factorial(num) {
  if (num > 1) {
    return num * factorial(num - 1);
  }
  return 1;
}

if (!isNaN(num)) {
  console.log(factorial(num));
} else console.log('1');
