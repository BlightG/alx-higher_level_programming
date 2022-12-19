#!/usr/bin/node
const { argv } = require("process");

let number = argv.length;
if (number < 3) {
  console.log("No argument");
} else {
  console.log("Argument found");
}
