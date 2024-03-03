const fs = require('fs');
const input = fs.readFileSync(process.platform === "linux" ? "dev/stdin" : "input.txt").toString().split("\n").map(el => el.trim().split(' ').map(Number))

const [N,M] = input.shift()
let matrix = new Array(N).fill().map(() => new Array(M).fill(0))

for(i=0;i<N;i++)
{
    for(j=0;j<M;j++)
    {
        matrix[i][j] = input[i][j] + input[i+N][j]
    }
}

for (const row of matrix)
{
    console.log(row.join(' '))
}