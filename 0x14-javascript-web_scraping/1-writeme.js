#!/usr/bin/node

const fs = require('fs');

/**
 * Writes content to a file.
 * @param {string} filePath - The path of the file to write to.
 * @param {string} content - The content to write to the file.
 */
fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
