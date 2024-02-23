package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var writer = bufio.NewWriter(os.Stdout)
var reader = bufio.NewReader(os.Stdin)

func scanf(f string, a ...interface{})  { fmt.Fscanf(reader, f, a...) }
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }

type Point struct {
	x, y int
}

func main() {
	defer writer.Flush()
	var n int
	scanf("%d\n", &n)

	points := make([]Point, n)
	for i := 0; i < n; i++ {
		scanf("%d %d\n", &points[i].x, &points[i].y)
	}

	sort.Slice(points, func(i, j int) bool {
		if points[i].y == points[j].y {
			return points[i].x < points[j].x
		}
		return points[i].y < points[j].y
	})

	// Print sorted points
	for _, p := range points {
		printf("%d %d\n", p.x, p.y)
	}
}