package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n int
	fmt.Fscan(reader, &n)

	for i := 0; i < n; i++ {
		var a, b int64
		fmt.Fscan(reader, &b, &a)

		result := big.NewInt(1)
		result.Binomial(a, b)

		fmt.Fprintln(writer, result)
	}
}