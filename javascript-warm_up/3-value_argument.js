#!/usr/bin/node

const arg1 = process.argv[2];

if (arg1) {
  console.log(`First argument: ${arg1}`);
} else {
  console.log('No argument');
}
