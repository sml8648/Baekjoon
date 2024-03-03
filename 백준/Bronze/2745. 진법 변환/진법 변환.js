const fs = require('fs');
const input = fs.readFileSync(process.platform === "linux" ? "dev/stdin" : "input.txt").toString().split(" ")

let number = input[0].split("").reverse()
let base = parseInt(input[1])

let base_obj = {}
for(i=0;i<36;i++){

    if (i >= 10){
        base_obj[String.fromCharCode(i+55)] = i
    }else {
        base_obj[i] = i
    }
}

let result = 0
for(i=0;i<number.length;i++)
{
    tmp = (base**i)*(base_obj[number[i]])
    result += tmp
}

console.log(result)