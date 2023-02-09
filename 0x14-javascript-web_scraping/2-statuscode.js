#!/usr/bin/node

const request = require('request');
const { argv } = require('process');

request
  .get(argv[2])
  .on('response', function (response) {
    console.log('Code: ', response.statusCode); // 200
    // console.log(response.headers['content-type']) 'image/png'
  });
