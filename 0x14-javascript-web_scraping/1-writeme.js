#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process')

let fInput = argv[3] + '\n'
fs.writeFile(argv[2], fInput, (err) => {
   if (err) throw err;
})
