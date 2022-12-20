#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let elementcount = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      elementcount += 1;
    }
  }
  return elementcount;
};
