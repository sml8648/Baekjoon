package main

import (
	"fmt"
	"sort"
)

func main() {
	var N, k int
	fmt.Scan(&N, &k)

	scores := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&scores[i])
	}

	// 점수를 내림차순으로 정렬
	sort.Sort(sort.Reverse(sort.IntSlice(scores)))

	// 상을 받는 커트라인을 찾음
	cutline := scores[k-1]
	fmt.Println(cutline)
}