const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split(' ');

const A = parseInt(inputData[0]);

if (A % 4 == 0){

    if ((A%100 != 0) || (A%400 == 0)){
        console.log(1);
    } else {
        console.log(0);
    }
} else {
    console.log(0);
}