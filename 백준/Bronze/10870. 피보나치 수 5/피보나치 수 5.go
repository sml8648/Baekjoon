package main

import (
	"bufio"
	"fmt"
	"os"
)

func fibonachi(n int) int {
	if n == 0 {
		return 0
	} else if n == 1 {
		return 1
	} else if n == 2 {
		return 1
	}

	return fibonachi(n-1) + fibonachi(n-2)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n int
	fmt.Fscan(reader, &n)

	result := fibonachi(n)

	fmt.Println(result)

}