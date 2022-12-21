#!/usr/bin/node
const { argv } = require('process');

function add (a, b) {
  console.log(num1 + num2);
}
const num1 = parseInt(argv[2], 10);
const num2 = parseInt(argv[3], 10);
add(num1, num2);
