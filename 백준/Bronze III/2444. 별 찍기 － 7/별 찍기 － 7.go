package main

import (
	"fmt"
)

func main() {

	var m int
	fmt.Scan(&m)

	n := 2*(m-1) + 1
	for i := 1; i <= n; i++ {

		num_star := 2*(i-1) + 1
		if i <= m {
			void_space := (n - num_star) / 2

			for j := 0; j < void_space; j++ {
				fmt.Print(" ")
			}

			for k := 0; k < num_star; k++ {
				fmt.Print("*")
			}
			fmt.Println()

		} else {
			diff := num_star - n
			void_space := diff / 2

			for j := 0; j < void_space; j++ {
				fmt.Print(" ")
			}

			for k := 0; k < n-diff; k++ {
				fmt.Print("*")
			}
			fmt.Println()
		}
	}
}