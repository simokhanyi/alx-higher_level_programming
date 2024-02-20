#!/usr/bin/node
const fs = require('fs');

/**
 * Read and print the content of a file.
 * @param {string} filePath - The path of the file to read.
 */
function readFileContent(filePath) {
  // Read the content of the file in utf-8 encoding
  fs.readFile(filePath, 'utf-8', (err, data) => {
    // Handle error if occurred during reading
    if (err) {
      console.error(err);
      return;
    }
    // Print the content of the file
    console.log(data);
  });
}

// Get the file path from command line argument
const filePath = process.argv[2];

// Call the function to read and print file content
readFileContent(filePath);
