package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	total := 0.0
	sum := 0.0

	for i := 0; i < 20; i++ {
		scanner.Scan()
		input := scanner.Text()
		results := strings.Split(input, " ")
		count, _ := strconv.ParseFloat(results[1], 32)

		total += count
		if results[2] == "A+" {
			sum += (count * 4.5)
		} else if results[2] == "A0" {
			sum += (count * 4)
		} else if results[2] == "B+" {
			sum += (count * 3.5)
		} else if results[2] == "B0" {
			sum += (count * 3)
		} else if results[2] == "C+" {
			sum += (count * 2.5)
		} else if results[2] == "C0" {
			sum += (count * 2)
		} else if results[2] == "D+" {
			sum += (count * 1.5)
		} else if results[2] == "D0" {
			sum += (count * 1)
		} else if results[2] == "F" {
			sum += 0
		} else if results[2] == "P" {
			total -= count
		}
	}

	// fmt.Println(total)
	// fmt.Println(sum)
	fmt.Println(sum / total)
}