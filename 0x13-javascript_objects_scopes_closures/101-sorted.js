#!/usr/bin/node
const data = require('./101-data').dict;

const newdata = Object.keys(data).map(function(key) {
  return [key, data[key]];
});

console.log(newdata);