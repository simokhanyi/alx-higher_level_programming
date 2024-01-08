#!/usr/bin/node

const args = process.argv.slice(2);
const firstArg = args[0];

if (Number.isInteger(Number(firstArg))) {
  console.log(`My number: ${parseInt(firstArg, 10)}`);
} else {
  console.log('Not a number');
}
