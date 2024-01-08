#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  let largest = args[0];
  let secondLargest = -Infinity;

  for (let i = 1; i < args.length; i++) {
    if (args[i] > largest) {
      secondLargest = largest;
      largest = args[i];
    } else if (args[i] > secondLargest && args[i] !== largest) {
      secondLargest = args[i];
    }
  }

  if (secondLargest === -Infinity) {
    console.log(0);
  } else {
    console.log(secondLargest);
  }
}
