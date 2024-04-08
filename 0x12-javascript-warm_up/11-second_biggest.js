#!/usr/bin/node
const len = process.argv.slice(2);

// convert arguments to numbers
const numbers = len.map(Number);

let big;
if (numbers.length < 2) {
  big = 0;
} else {
  numbers.sort((a, b) => a - b);
  big = numbers[numbers.length - 2];
}
console.log(big);
