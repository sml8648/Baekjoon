const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const A = inputData[0];
for(let i = 1;i<=9;i++){
    console.log(`${A} * ${i} = ${A*i}`)
}