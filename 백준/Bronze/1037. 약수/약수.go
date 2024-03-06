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

	var n int
	fmt.Fscan(reader, &n)

	max := -1
	min := 9999999
	for i := 0; i < n; i++ {
		var t int
		fmt.Fscan(reader, &t)
		if t > max {
			max = t
		}
		if t < min {
			min = t
		}
	}

	fmt.Fprintln(writer, max*min)
}