#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jBody = JSON.parse(body);
    const dictUser = {};
    for (const allTask of jBody) {
      if (allTask.completed) {
        if (dictUser[allTask.userId]) {
          dictUser[allTask.userId] += 1;
        } else {
          dictUser[allTask.userId] = 1;
        }
      }
    }
    console.log(dictUser);
  }
});
