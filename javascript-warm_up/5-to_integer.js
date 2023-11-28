#!/usr/bin/node

const arg1 = process.argv[2];
const int1 = parseInt(arg1);

if (!isNaN(int1)) {
  console.log(`My number: ${int1}`);
} else {
  console.log('Not a number');
}
