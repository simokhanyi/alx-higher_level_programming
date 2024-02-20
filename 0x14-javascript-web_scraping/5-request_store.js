#!/usr/bin/node

const request = require('request');
const fs = require('fs');

/**
 * Fetches the contents of a webpage and stores it in a file.
 * @param {string} url - The URL of the webpage to request.
 * @param {string} filePath - The file path to store the response body.
 */
function requestAndStore (url, filePath) {
  // Make a GET request to the specified URL
  request.get(url, (error, response, body) => {
    // Handle error if occurred during request
    if (error) {
      console.error(error);
      return;
    }
    // Write the response body to the specified file path
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      // Handle error if occurred during writing
      if (err) {
        console.error(err);
        return;
      }
      console.log(`Content has been stored in ${filePath} successfully.`);
    });
  });
}

// Get the URL and file path from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Call the function to fetch webpage contents and store them in a file
requestAndStore(url, filePath);
