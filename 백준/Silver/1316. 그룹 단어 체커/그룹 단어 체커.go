package main

import (
	"fmt"
)

func main() {

	var n int
	_, err := fmt.Scan(&n)

	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	total_count := 0
	for i := 0; i < n; i++ {

		var inputs string
		fmt.Scan(&inputs)

		var before rune = 'Z'
		charCount := make(map[rune]int)

		flag := true
		for _, input := range inputs {

			count, _ := charCount[input]
			charCount[input]++
			if count != 0 && before != input {
				flag = false
				break
			}
			before = input

		}

		if flag {
			total_count++
		}

	}

	fmt.Println(total_count)

}