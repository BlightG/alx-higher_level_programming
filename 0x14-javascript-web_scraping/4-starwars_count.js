#!/usr/bin/node

const request = require('request');
const { argv } = require('process');

let count = 0;

request(argv[2], (error, response, body) => {
  if (error) console.log(error);
  // console.log(response.statusCode);
  const jsondict = JSON.parse(body);
  for (let i = 0; i < jsondict.results.length; i++) {
    // console.log(jsondict['results'][i]);
    for (let j = 0; j < jsondict.results[i].characters.length; j++) {
      // console.log(typeof jsondict['results'][i]['characters'][j]);
      if (jsondict.results[i].characters[j] ===
             'https://swapi-api.alx-tools.com/api/people/18/') {
        count += 1;
      }
    }
  }
  console.log(count);
});
