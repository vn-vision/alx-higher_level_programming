#!/usr/bin/node
const x = Number(process.argv[2] | 0);

if (x) {
  if (x > 0) {
    for (let i = 0; i < x; i++) {
      let row = '';
      for (let j = 0; j < x; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
} else {
  console.log('Missing size');
}
