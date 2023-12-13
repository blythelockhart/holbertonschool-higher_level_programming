#!/usr/bin/node

const request = require('request');

// Check if the API URL is provided as an argument
if (process.argv.length < 3) {
  console.error('Usage: node script.js <api-url>');
  process.exit(1);
}

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the Star Wars API films endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Parse the JSON response
    const filmsData = JSON.parse(body);

    // Check if the results contain films
    if (filmsData.results) {
      // Count the number of films where Wedge Antilles is present (character ID 18)
      const wedgeFilms = filmsData.results.filter(film => film.characters.some(character => character.includes('/18/')));
      // const wedgeFilms = filmsData.results.filter(film => film.characters.includes('https://swapi-api.hbtn.io/api/people/18'));
      
      console.log(`${wedgeFilms.length}`);
    } else {
      console.error('Error retrieving films data from the API.');
    }
  }
});
