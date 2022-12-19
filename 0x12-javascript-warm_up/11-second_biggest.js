#!/usr/bin/node
const { argv } = require("process");

function second_max(argv) {
  let list_num = argv.length;
  let max = 0;
  let second_max = 0;
  for (let i = 2; i < list_num; i++) {
    let num = parseInt(argv[i], 10);
    if (num >= second_max && num < max) {
      second_max = num;
    } else if (num > max) {
      second_max = max;
      max = num;
    }
  }
  return second_max;
}
if (argv[2] == null) {
  console.log("0");
} else if (argv[3] == null) {
  console.log("0");
} else {
  console.log(second_max(argv));
}
