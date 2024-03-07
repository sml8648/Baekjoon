package main

import (
	"bufio"
	"fmt"
	"os"
)

var globalCount int = 0

func fibonacchi(n int) int {
	if n == 1 || n == 2 {
		globalCount++
		return 1
	} else {
		return fibonacchi(n-1) + fibonacchi(n-2)
	}
}
func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n int
	fmt.Fscan(reader, &n)

	fibonacchi(n)
	fmt.Fprint(writer, globalCount, n-2)
}