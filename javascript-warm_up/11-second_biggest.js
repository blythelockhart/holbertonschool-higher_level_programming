#!/usr/bin/node

const args = process.argv.slice(2);
const argc = args.length;

if (argc === 0 || argc === 1) {
  console.log(0);
} else {
  const ints = args.map(Number).sort((a, b) => b - a);

  console.log(ints[1]);
}
