const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const a = inputData.map(x => parseInt(x))

let max = -1
let index = -1

a.forEach((number, idx) => {
    if (number > max) {
        max = number
        index = idx
    }
})

console.log(max);
console.log(index+1);