#!/usr/bin/node


const request = require('request');

/**
 * Prints the number of movies where the character "Wedge Antilles" is present.
 * @param {string} apiUrl - The API URL of the Star Wars API films endpoint.
 */
function countMoviesWithWedgeAntilles(apiUrl) {
  // Make a GET request to the Star Wars API films endpoint
  request.get(apiUrl, (error, response, body) => {
    // Handle error if occurred during request
    if (error) {
      console.error(error);
      return;
    }
    // Parse the JSON response
    const films = JSON.parse(body).results;

    // Filter films where Wedge Antilles is present
    const moviesWithWedgeAntilles = films.filter(film =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );

    // Print the number of movies where Wedge Antilles is present
    console.log(moviesWithWedgeAntilles.length);
  });
}

// Get the API URL from command line argument
const apiUrl = process.argv[2];

// Call the function to print the number of movies with Wedge Antilles
countMoviesWithWedgeAntilles(apiUrl);
