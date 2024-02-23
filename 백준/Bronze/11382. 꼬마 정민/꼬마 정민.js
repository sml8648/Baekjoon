const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split(' ');

const A = parseInt(inputData[0]);
const B_1 = parseInt(inputData[1]);
const B_2 = parseInt(inputData[2]);

console.log(A + B_1 + B_2);