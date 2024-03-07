package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n, m int
	reader := bufio.NewReader(os.Stdin)
	fmt.Fscanln(reader, &n, &m)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	// var visited = make([]bool, n+1)
	var result = make([]int, m+1)

	sequence(writer, result, 0, n, m)
}

func sequence(writer *bufio.Writer, result []int, index, n, m int) {
	if index == m { // if result array is full
		for i := 0; i < m; i++ {
			fmt.Fprintf(writer, "%d ", result[i])
		}
		fmt.Fprint(writer, "\n")
		return
	}
	for i := 1; i < n+1; i++ {

		if index == 0 {
			result[index] = i
			sequence(writer, result, index+1, n, m)
		} else {
			if result[index-1] < i {
				result[index] = i
				sequence(writer, result, index+1, n, m)
			}
		}
	}
}