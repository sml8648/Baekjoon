package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)

	for i := 0; i < n; i++ {
		var num int
		fmt.Scan(&num)

		var result []int
		quarter := num / 25
		num = num % 25
		result = append(result, quarter)

		dime := num / 10
		num = num % 10
		result = append(result, dime)

		nickel := num / 5
		num = num % 5
		result = append(result, nickel)

		penny := num / 1
		result = append(result, penny)

		for _, each := range result {
			fmt.Print(each, " ")
		}
		fmt.Println()

	}
}