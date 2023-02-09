#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process');
const request = require('request');

request(argv[2], (error, response, body) => {
  if (error) console.log(error);
  // const fInput = response.statusCode;
  fs.writeFile(argv[3], body, (err) => {
    if (err) throw err;
  });
});
