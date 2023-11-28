#!/usr/bin/node

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const arg1 = parseInt(process.argv[2]);

if (!isNaN(arg1)) {
  console.log(factorial(arg1));
} else {
  console.log(1);
}
