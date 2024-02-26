const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const a = parseInt(inputData[0]);
const b = inputData[1].split(' ').map(x => parseInt(x));

b.sort((a,b) => a - b);

console.log(`${b[0]} ${b[a - 1]}`);