#!/usr/bin/node

const request = require('request');
const fs = require('fs');

function fetchAndSave (url, filePath) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(`Content has been saved to ${filePath} successfully.`);
    });
  });
}

const url = process.argv[2];
const filePath = process.argv[3];

fetchAndSave(url, filePath);
