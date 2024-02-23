package main

import (
	"bufio"
	"fmt"
	"os"
)

var writer = bufio.NewWriter(os.Stdout)
var reader = bufio.NewReader(os.Stdin)

func scanf(f string, a ...interface{})  { fmt.Fscanf(reader, f, a...) }
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }

func main() {
	defer writer.Flush()
	var n int
	scanf("%d\n", &n)

	result := make(map[int]int, 10001)
	for i := 0; i < n; i++ {
		var t int
		scanf("%d\n", &t)
		result[t]++
	}

	for i := 1; i <= 10000; i++ {

		if result[i] > 0 {
			for j := 0; j < result[i]; j++ {
				printf("%d\n", i)
			}
		}
	}
}