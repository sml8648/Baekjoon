const fs = require('fs');
const input = fs.readFileSync(process.platform === "linux" ? "dev/stdin" : "input.txt").toString().split(' ').map(Number)

const dividor = input[0] - input[1]
const result = Math.ceil((input[2] - input[0]) / dividor)

console.log(result + 1)