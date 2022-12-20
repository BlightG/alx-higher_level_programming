#!/usr/bin/node

exports.esrever = function (list) {
  const newlist = [];
  for (let i = 1; i <= list.length; i++) {
    newlist.push(list[list.length - i]);
  }
  return newlist;
};
