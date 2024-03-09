package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func biSearch(arr []int, n int) int {

	start := 0
	end := len(arr) - 1

	for {

		mid := (start + end) / 2
		if arr[mid] == n {
			return 1
		} else if start > end {
			break
		} else if arr[mid] < n {
			start = mid + 1
		} else if arr[mid] > n {
			end = mid - 1
		}
	}

	return 0
}

func main() {

	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var N int
	fmt.Fscan(reader, &N)
	arr := make([]int, N)

	for i := 0; i < N; i++ {
		fmt.Fscan(reader, &arr[i])
	}

	sort.Ints(arr)

	var M int
	fmt.Fscan(reader, &M)
	for i := 0; i < M; i++ {
		var t int
		fmt.Fscan(reader, &t)
		result := biSearch(arr, t)
		fmt.Fprintln(writer, result)
	}
}