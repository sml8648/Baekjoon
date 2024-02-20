package main

import (
	"fmt"
)

func base36Value(c byte) int {
	if c >= '0' && c <= '9' {
		return int(c - '0')
	}
	return int(c - 'A' + 10)
}

func baseToDecimal(num string, base int) int {
	decimal := 0
	for i := 0; i < len(num); i++ {
		decimal *= base
		decimal += base36Value(num[i])
	}
	return decimal
}

func main() {
	var num string
	var base int
	fmt.Scan(&num, &base)

	decimal := baseToDecimal(num, base)
	fmt.Println(decimal)
}
