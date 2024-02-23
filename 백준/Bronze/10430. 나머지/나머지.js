const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split(' ');

const A = parseInt(inputData[0]);
const B = parseInt(inputData[1]);
const C = parseInt(inputData[2]);

console.log((A+B)%C);
console.log(((A%C) + (B%C))%C);
console.log((A*B)%C);
console.log(((A%C) * (B%C))%C);