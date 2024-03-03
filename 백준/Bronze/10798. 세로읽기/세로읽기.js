const fs = require('fs');
const input = fs.readFileSync(process.platform === "linux" ? "dev/stdin" : "input.txt").toString().split("\n").map(el => el.trim())

const x = input.length
let max_y = -1
for (const row of input)
{
    if (row.length > max_y){
        max_y = row.length
    }
}

let answer = ""
for (i=0;i<max_y;i++){
    for(j=0;j<x;j++){
        if(input[j][i] != undefined){
            answer += input[j][i]
        }
    }
}

console.log(answer)