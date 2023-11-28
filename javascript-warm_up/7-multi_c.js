#!/usr/bin/node

const arg1 = process.argv[2];
const int1 = parseInt(arg1);

if (!isNaN(int1)) {
  for (let i = 0; i < int1; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
