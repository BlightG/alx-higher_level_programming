#!/usr/bin/node
const { argv } = require('process');

if (argv[2] == null) {
  console.log('No argument');
} else {
  argv
    .filter((element, index) => index > 1)
    .forEach((element) => console.log(element));
}
