#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const destinationFile = process.argv[4];

// Read content from fileA
fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) throw err;

  // Read content from fileB
  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) throw err;

    // Concatenate data from both files
    const concatenatedData = dataA + dataB;

    // Write concatenated data to the destination file
    fs.writeFile(destinationFile, concatenatedData, 'utf8', (err) => {
      if (err) throw err;
      console.log(`The content has been concatenated and written to ${destinationFile}`);
    });
  });
});
