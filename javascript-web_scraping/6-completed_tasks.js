#!/usr/bin/node

const request = require('request');

// Check if the API URL is provided as an argument
if (process.argv.length < 3) {
  console.error('Usage: node script.js <api-url>');
  process.exit(1);
}

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the JSONPlaceholder API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Parse the JSON response
    const todosData = JSON.parse(body);

    // Count completed tasks by user id
    const completedCount = {};

    todosData.forEach(task => {
      if (task.completed) {
        const userId = task.userId;

        completedCount[userId] = (completedCount[userId] || 0) + 1;
      }
    });
    // Print the result in JSON format
    console.log(JSON.stringify(completedCount, null, 2));
  }
});
