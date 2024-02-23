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
	var n, k int
	scanf("%d %d\n", &n, &k)

	var result []int
	for i := 1; i <= n; i++ {

		if (n % i) == 0 {
			result = append(result, i)
		}
	}

	if len(result) >= k {
		printf("%d\n", result[k-1])
	} else {
		printf("%d\n", 0)
	}
}