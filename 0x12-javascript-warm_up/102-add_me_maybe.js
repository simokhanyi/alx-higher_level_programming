#!/usr/bin/node

module.exports = function add(number, theFunction) {
  number++;
  theFunction(number);
};
