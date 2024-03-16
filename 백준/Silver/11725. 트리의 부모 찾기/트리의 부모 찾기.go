package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	graph   map[int][]int
	parents []int
	visited []bool
)

func main() {

	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n int
	fmt.Fscan(reader, &n)

	// Initialize graph and parents slice
	graph = make(map[int][]int, n)
	parents = make([]int, n+1)
	visited = make([]bool, n+1)

	// Read edges and construct the graph
	for i := 0; i < n-1; i++ {
		var u, v int
		fmt.Fscan(reader, &u, &v)
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}

	// DFS to find parents
	dfs(1, -1)

	// Print the parents except for the root
	for i := 2; i <= n; i++ {
		fmt.Fprintln(writer, parents[i])
	}
}

func dfs(node, parent int) {
	visited[node] = true
	parents[node] = parent

	for _, neighbor := range graph[node] {
		if !visited[neighbor] {
			dfs(neighbor, node)
		}
	}
}