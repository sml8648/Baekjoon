package main

import "fmt"

func main() {
	// Read input
	var words [5]string
	for i := 0; i < 5; i++ {
		fmt.Scan(&words[i])
	}

	// Find the maximum length of any word
	maxLen := 0
	for _, word := range words {
		if len(word) > maxLen {
			maxLen = len(word)
		}
	}

	// Initialize result string
	result := ""

	// Iterate through each column
	for col := 0; col < maxLen; col++ {
		// Iterate through each row
		for row := 0; row < 5; row++ {
			// Append character if it exists in this column
			if col < len(words[row]) {
				result += string(words[row][col])
			}
		}
	}

	// Print the result
	fmt.Println(result)
}
