const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = inputData[0]

for(i=0;i<n;i++)
{
    const len = inputData[i+1].trim().length;
    let result = '';

    result += inputData[i+1][0]
    result += inputData[i+1][len-1]

    console.log(result)

}