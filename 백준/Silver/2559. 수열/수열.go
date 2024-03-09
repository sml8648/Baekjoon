package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {

	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var N, L int
	fmt.Fscan(reader, &N, &L)
	arr := make([]int, N+1)
	arr[0] = 0
	for i := 0; i < N; i++ {
		var t int
		fmt.Fscan(reader, &t)
		arr[i+1] = t
	}

	for i := 1; i <= N; i++ {
		arr[i] = arr[i] + arr[i-1]
	}

	max := -9999999
	for i := L; i <= N; i++ {
		if (arr[i] - arr[i-L]) > max {
			max = (arr[i] - arr[i-L])
		}
	}
	fmt.Fprint(writer, max)
}