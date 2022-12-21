#!/usr/bin/node
const { argv } = require('process');

const num = parseInt(argv[2], 10);

if (num) {
  console.log(num);
} else console.log('Not a number');
