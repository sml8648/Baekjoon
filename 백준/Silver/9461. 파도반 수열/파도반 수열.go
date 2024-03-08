package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var dp [101]int
	dp[1] = 1
	dp[2] = 1
	dp[3] = 1

	for i := 4; i <= 100; i++ {
		dp[i] = dp[i-2] + dp[i-3]
	}

	var n int
	fmt.Fscanln(reader, &n)

	for i := 0; i < n; i++ {
		var m int
		fmt.Fscan(reader, &m)
		fmt.Fprintln(writer, dp[m])
	}

}