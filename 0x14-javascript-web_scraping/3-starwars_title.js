#!/usr/bin/node

const request = require('request');

/**
 * Prints the title of a Star Wars movie where the episode number matches a given integer.
 * @param {number} movieId - The episode number of the Star Wars movie.
 */
function printMovieTitle (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  // Make a GET request to the Star Wars API
  request.get(url, (error, response, body) => {
    // Handle error if occurred during request
    if (error) {
      console.error(error);
      return;
    }
    // Parse the JSON response
    const movie = JSON.parse(body);
    // Print the title of the movie
    console.log(movie.title);
  });
}

// Get the movie ID from command line argument
const movieId = process.argv[2];

// Call the function to print the title of the Star Wars movie
printMovieTitle(movieId);
