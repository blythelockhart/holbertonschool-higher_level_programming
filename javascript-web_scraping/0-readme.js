#!/usr/bin/node

const fs = require('fs');

// Check if the file path is provided as an argument
if (process.argv.length < 3) {
  console.error('Usage: node script.js <file-path>');
  process.exit(1);
}

// Get the file path from the command line arguments
const filePath = process.argv[2];

// Read the content of the file in utf-8
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // Print the error object if an error occurred
    console.error(err);
  } else {
    // Print the content of the file
    console.log(data);
  }
});
