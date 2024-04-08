#!/usr/bin/node
let big = 0;
const len = process.argv.slice(2);

if (len && len > 1) {
// convert arguments to numbers
  const numbers = len.map(Number);

  numbers.sort((a, b) => a - b);

  big = numbers[numbers.length - 2];
}
console.log(big);
