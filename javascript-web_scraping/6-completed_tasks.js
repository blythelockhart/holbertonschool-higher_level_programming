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

    // Filter completed tasks
    const completedTasks = todosData.filter(task => task.completed);

    // Create a map to count completed tasks by user id
    const completedCountByUserId = new Map();

    completedTasks.forEach(task => {
      const userId = task.userId;

      completedCountByUserId.set(userId, (completedCountByUserId.get(userId) || 0) + 1);
    });

    // Print the number of completed tasks by user id
    completedCountByUserId.forEach((count, userId) => {
      console.log(`'${userId}': ${count}`);
    });
  }
});

