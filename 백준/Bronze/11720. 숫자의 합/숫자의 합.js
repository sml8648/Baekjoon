const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = inputData[0]
let sum = 0;
for(i=0;i<n;i++){
    sum += Number(inputData[1][i]);
}

console.log(sum);