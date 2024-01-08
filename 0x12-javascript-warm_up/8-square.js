#!/usr/bin/node

const args = process.argv.slice(2);
const size = parseInt(args[0]);

if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  if (size > 0) {
    for (let i = 0; i < size; i++) {
      console.log('X'.repeat(size));
    }
  }
}
