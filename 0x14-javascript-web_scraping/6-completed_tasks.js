#!/usr/bin/node

const request = require('request');

/**
 * Computes the number of tasks completed by user id.
 * @param {string} apiUrl - The API URL to fetch the tasks data.
 */
function computeCompletedTasks (apiUrl) {
  // Make a GET request to the specified API URL
  request.get(apiUrl, (error, response, body) => {
    // Handle error if occurred during request
    if (error) {
      console.error(error);
      return;
    }
    // Parse the JSON response
    const tasks = JSON.parse(body);

    // Create an object to store the count of completed tasks per user
    const completedTasksByUser = {};

    // Iterate through the tasks and count completed tasks per user
    tasks.forEach(task => {
      if (task.completed) {
        if (completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId]++;
        } else {
          completedTasksByUser[task.userId] = 1;
        }
      }
    });

    // Print the count of completed tasks per user
    console.log(completedTasksByUser);
  });
}

// Get the API URL from command line argument
const apiUrl = process.argv[2];

// Call the function to compute completed tasks by user id
computeCompletedTasks(apiUrl);
