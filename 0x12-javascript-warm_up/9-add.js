#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const args = process.argv.slice(2);
const firstInteger = parseInt(args[0]);
const secondInteger = parseInt(args[1]);

if (Number.isNaN(firstInteger) || Number.isNaN(secondInteger)) {
  console.log('NaN');
} else {
  const result = add(firstInteger, secondInteger);
  console.log(result);
}
