#!/usr/bin/node

if (Number(process.argv[2] | 0)) {
  console.log('My number: ' + Number(process.argv[2] | 0));
} else {
  console.log('Not a number');
}
