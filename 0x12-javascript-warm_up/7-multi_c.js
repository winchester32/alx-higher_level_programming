#!/usr/bin/node
const word = 'C is fun';
const num = Math.floor(Number(process.argv[2]));
if (isNaN(num) === true) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log(word);
  }
}
