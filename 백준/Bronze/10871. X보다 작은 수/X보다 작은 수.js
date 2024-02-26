const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const a = inputData[0].split(' ').map(x => parseInt(x));
const b = inputData[1].split(' ').map(x => parseInt(x));

const answer = b.filter(x => x < a[1] );

console.log(answer.join(' '));