package main

import (
	"bufio"
	"fmt"
	"os"
)

var writer = bufio.NewWriter(os.Stdout)
var reader = bufio.NewReader(os.Stdin)

func scanf(f string, a ...interface{})  { fmt.Fscanf(reader, f, a...) }
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }

func main() {
	defer writer.Flush()

	var n int
	scanf("%d\n", &n)

	fmt.Println(n * n)
	fmt.Println(2)
}