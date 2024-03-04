package main

import (
	"bufio"
	"fmt"
	"os"
)

func gcdFunc(a, b int) int {
	for a > 0 {
		a, b = b%a, a
	}
	return b
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var a, b int
	fmt.Fscan(reader, &a, &b)
	gcd := gcdFunc(a, b)

	fmt.Println((a * b) / gcd)
}