const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const input_string = inputData[0];
const idx = inputData[1];

console.log(input_string[idx - 1]);