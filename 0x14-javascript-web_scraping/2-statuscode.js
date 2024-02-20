#!/usr/bin/node

const request = require('request');

/**
 * Display the status code of a GET request to a specified URL.
 * @param {string} url - The URL to request.
 */
function displayStatusCode (url) {
  // Make a GET request to the specified URL
  request.get(url, (error, response) => {
    // Handle error if occurred during request
    if (error) {
      console.error(error);
      return;
    }
    // Print the status code of the response
    console.log(`code: ${response.statusCode}`);
  });
}

// Get the URL from command line argument
const url = process.argv[2];

// Call the function to display status code of the request
displayStatusCode(url);
