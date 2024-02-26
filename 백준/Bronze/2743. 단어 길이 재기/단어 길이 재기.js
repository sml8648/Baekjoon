const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const input_string = inputData[0];

console.log(input_string.length);