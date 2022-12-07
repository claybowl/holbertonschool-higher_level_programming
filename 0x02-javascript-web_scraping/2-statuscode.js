#!/usr/bin/node
const request = require('request');
const https = require('https');
const url = process.argv[2];
https.get(url, res => {
  console.log(`code: ${res.statusCode}`);
});
