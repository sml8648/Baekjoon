package main

import (
	"fmt"
	"sort"
)

func main() {

	var n int
	fmt.Scan(&n)

	var result []int
	for i := 0; i < n; i++ {
		var t int
		fmt.Scan(&t)
		result = append(result, t)
	}

	sort.Ints(result)

	for _, each := range result {
		fmt.Println(each)
	}
}
