package main

import (
	"fmt"
	"sort"
)

var (
	graph   map[int][]int
	visited map[int]bool
	count   int = 0
)

func main() {
	var N int
	fmt.Scan(&N)

	var M int
	fmt.Scan(&M)

	graph = make(map[int][]int)
	visited = make(map[int]bool)

	for i := 0; i < M; i++ {
		var u, v int
		fmt.Scan(&u, &v)
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}

	for key := range graph {
		sort.Ints(graph[key])
	}

	dfs(1)
	fmt.Println(count - 1)
}

func dfs(node int) {
	if visited[node] {
		return
	}

	count++
	visited[node] = true

	for _, neighbor := range graph[node] {
		dfs(neighbor)
	}
}