const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = inputData[0];
for(let i = 1;i<=n;i++){
    let tmp = inputData[i].split(' ');
    console.log(parseInt(tmp[0])+ parseInt(tmp[1]));
}