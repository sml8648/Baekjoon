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

	bucket := make(map[string]bool)
	count := 0
	for i := 0; i < n; i++ {
		var s string
		fmt.Fscan(reader, &s)

		if s == "ENTER" {
			bucket = make(map[string]bool)
		} else {
			if !bucket[s] {
				count++
				bucket[s] = true
			}
		}
	}

	fmt.Fprintln(writer, count)
}