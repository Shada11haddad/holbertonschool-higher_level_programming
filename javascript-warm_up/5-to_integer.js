#!/usr/bin/node

const n = process.argv[2];

if (isNaN(parseInt(n))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(n));
}
