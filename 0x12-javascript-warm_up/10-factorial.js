#!/usr/bin/node

const a = Number(process.argv[2] | 0);

function factorial (n) {
  // create base for the recursion
  if (n === 0 || n === 1) {
    return 1;
  }

  // call the function factorial inside itself
  // pass it the value n - 1

  return (n * factorial(n - 1));
}

console.log(factorial(a));
