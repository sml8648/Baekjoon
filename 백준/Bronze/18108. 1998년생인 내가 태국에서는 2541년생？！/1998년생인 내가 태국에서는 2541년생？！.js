const fs = require('fs');
const inputData = fs.readFileSync('/dev/stdin','utf8').toString().trim()

const tmp = parseInt(inputData)

console.log(tmp -543)
