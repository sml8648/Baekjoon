package main

import (
	"fmt"
)

func main() {

	n := 9
	m := 9
	matrix := make([][]int, n)

	for i := 0; i < n; i++ {
		row := make([]int, m)
		for j := 0; j < m; j++ {
			var tmp int
			fmt.Scan(&tmp)
			row[j] = tmp
		}
		matrix[i] = row
	}

	max_value := -1
	position_x := -1
	position_y := -1

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if matrix[i][j] > max_value {
				max_value = matrix[i][j]
				position_x = i
				position_y = j
			}
		}
	}

	fmt.Println(max_value)
	fmt.Print(position_x+1, position_y+1)
}
