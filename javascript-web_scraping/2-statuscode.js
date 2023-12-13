#!/usr/bin/node

const request = require('request');

// Check if the URL is provided as an argument
if (process.argv.length < 3) {
  console.error('Usage: node script.js <URL>');
  process.exit(1);
}

// Get the URL from the command line arguments
const url = process.argv[2];

// Make a GET request to the specified URL
request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    // Display the status code
    console.log(`code: ${response.statusCode}`);
  }
});
