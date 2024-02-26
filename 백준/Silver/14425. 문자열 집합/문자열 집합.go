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

	var N, M int
	fmt.Fscan(reader, &N, &M)

	// Create a map to store the strings in set S
	setS := make(map[string]bool)

	// Read strings in set S
	for i := 0; i < N; i++ {
		var str string
		fmt.Fscan(reader, &str)
		setS[str] = true
	}
	count := 0

	// Check if strings are in set S
	for i := 0; i < M; i++ {
		var str string
		fmt.Fscan(reader, &str)
		if setS[str] {
			count++
		}
	}

	fmt.Println(count)
}