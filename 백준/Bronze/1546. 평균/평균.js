const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = parseInt(inputData[0]);
const arr = inputData[1].split(' ').map(x => parseInt(x));

arr.sort((a,b) => a - b)
const max = arr[n-1];

let new_arr = [];
arr.forEach((number) => {
    new_arr.push( (number /max)*100)
})

let sum = 0;
new_arr.forEach((number) => {
    sum += number
})

console.log(sum / n)