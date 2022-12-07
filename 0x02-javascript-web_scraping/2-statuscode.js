#!/usr/bin/node
const https = require('https');
// retrieves url for get request from command line argument
const url = process.argv[2];
https.get(url, res => {
  console.log('code: ${res.statusCode}');
});
