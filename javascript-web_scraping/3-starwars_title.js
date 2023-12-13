#!/usr/bin/node

const request = require('request');

// Check if the movie ID is provided as an argument
if (process.argv.length < 3) {
  console.error('Usage: node script.js <movie-id>');
  process.exit(1);
}

// Get the movie ID from the command line arguments
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

// Make a GET request to the Star Wars API with the specified movie ID
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Parse the JSON response
    const movieData = JSON.parse(body);

    // Check if the movie data contains a title
    if (movieData.title) {
      console.log(`${movieData.title}`);
    } else {
      console.error(`Movie with ID ${movieId} not found.`);
    }
  }
});
