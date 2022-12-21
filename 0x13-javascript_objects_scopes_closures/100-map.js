#!/usr/bin/node
const data = require('./100-data').list;

const newList = data.map((element, index) => element * index);
console.log(data);
console.log(newList);
