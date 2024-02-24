package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var writer = bufio.NewWriter(os.Stdout)
var reader = bufio.NewReader(os.Stdin)

func scanf(f string, a ...interface{})  { fmt.Fscanf(reader, f, a...) }
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }

func main() {
	defer writer.Flush()

	for {
		var n int
		scanf("%d\n", &n)

		if n == -1 {
			break
		}

		sum := 0
		var result []int
		for i := 1; i < n; i++ {
			if n%i == 0 {
				sum += i
				result = append(result, i)
			}
		}

		if sum == n {
			answer := ""
			for idx, each := range result {

				tmp := strconv.Itoa(each)
				answer += tmp

				if idx < (len(result) - 1) {
					answer += " + "
				}
			}
			fmt.Printf("%d = %s\n", n, answer)
		} else {
			fmt.Printf("%d is NOT perfect.\n", n)
		}
	}
}