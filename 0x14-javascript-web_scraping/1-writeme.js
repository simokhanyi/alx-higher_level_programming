#!/usr/bin/node


const fs = require('fs');

/**
 * Write a string to a file.
 * @param {string} filePath - The path of the file to write.
 * @param {string} content - The string content to write to the file.
 */
function writeToFile(filePath, content) {
  // Write the content to the file in utf-8 encoding
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    // Handle error if occurred during writing
    if (err) {
      console.error(err);
      return;
    }
    console.log('Content has been written to the file successfully.');
  });
}

// Get file path and content from command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Call the function to write content to the file
writeToFile(filePath, content);
