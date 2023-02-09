#!/usr/bin/node

const request = require('request');
const { argv } = require('process');

const url = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);
  // console.log(response.statusCode);
  const jsondict = JSON.parse(body);
  console.log(jsondict.title);
});
