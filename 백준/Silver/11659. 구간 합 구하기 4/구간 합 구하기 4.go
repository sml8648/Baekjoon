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

	for i := 0; i < L; i++ {
		var a, b int
		fmt.Fscan(reader, &a, &b)
		fmt.Fprintln(writer, arr[b]-arr[a-1])
	}
}