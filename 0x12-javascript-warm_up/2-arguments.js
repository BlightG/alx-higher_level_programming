#!/usr/bin/node

const { argv } = require('process');

const number = argv.length;
if (number < 3) {
  console.log('No argument');
} else if (number === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
