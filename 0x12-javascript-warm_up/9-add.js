#!/usr/bin/node
const { argv } = require('process');

function add(a, b) {
  console.log(num_1 + num_2);
}
let num_1 = parseInt(argv[2], 10);
let num_2 = parseInt(argv[3], 10);
add(num_1, num_2);

