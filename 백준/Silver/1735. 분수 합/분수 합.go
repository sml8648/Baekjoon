package main

import (
	"bufio"
	"fmt"
	"os"
)

func gcdFunc(a, b int) int {
	for a > 0 {
		a, b = b%a, a
	}
	return b
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var a, b int
	fmt.Fscanln(reader, &a, &b)

	var c, d int
	fmt.Fscanln(reader, &c, &d)

	numerator := a*d + c*b
	denominator := b * d

	divider := gcdFunc(numerator, denominator)

	fmt.Println(numerator/divider, denominator/divider)

}