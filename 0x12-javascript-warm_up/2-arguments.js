#!/usr/bin/node

const { argv } = require('process');

const number = argv.length;
if (number < 3) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
