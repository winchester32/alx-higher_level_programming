#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));
if (isNaN(num) === true) {
  console.log('Missing size');
} else {
  for (let r = 0; r < num; r++) {
    let row = '';
    for (let i = 0; i < num; i++) row += 'X';
    console.log(row);
  }
}
