#!/usr/bin/node

const countThewords = process.argv.length - 2;

if (countThewords === 0) {
  console.log('No argument');
} else if (countThewords === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
