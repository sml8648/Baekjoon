package main

import (
	"bufio"
	"fmt"
	"os"
)

var globalVar int = 0

func recursion(s string, l int, r int) int {
	globalVar += 1
	if l >= r {
		return 1
	} else if s[l] != s[r] {
		return 0
	} else {
		return recursion(s, l+1, r-1)
	}
}

func isPalindrome(s string) int {
	return recursion(s, 0, len(s)-1)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n int
	fmt.Fscan(reader, &n)

	for i := 0; i < n; i++ {
		var s string
		fmt.Fscan(reader, &s)
		result := isPalindrome(s)
		fmt.Fprintln(writer, result, globalVar)
		globalVar = 0
	}
}
