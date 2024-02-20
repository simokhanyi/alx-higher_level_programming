#!/usr/bin/node


const request = require('request');

/**
 * Prints all characters of a Star Wars movie.
 * @param {number} movieId - The ID of the Star Wars movie.
 */
function printMovieCharacters(movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  // Make a GET request to the specified Star Wars API endpoint
  request.get(apiUrl, (error, response, body) => {
    // Handle error if occurred during request
    if (error) {
      console.error(error);
      return;
    }
    // Parse the JSON response
    const movie = JSON.parse(body);

    // Array to store character names
    const characterNames = [];

    // Fetch character data for each character URL
    movie.characters.forEach(characterUrl => {
      request.get(characterUrl, (error, response, body) => {
        // Handle error if occurred during request
        if (error) {
          console.error(error);
          return;
        }
        // Parse the JSON response
        const character = JSON.parse(body);
        // Push character name to the array
        characterNames.push(character.name);

        // Print character name if all characters are fetched
        if (characterNames.length === movie.characters.length) {
          characterNames.forEach(name => console.log(name));
        }
      });
    });
  });
}

// Get the movie ID from command line argument
const movieId = process.argv[2];

// Call the function to print all characters of the Star Wars movie
printMovieCharacters(movieId);
