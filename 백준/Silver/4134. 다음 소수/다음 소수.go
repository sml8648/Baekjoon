package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func Prime(num int) bool {
	for i := 2; i*i <= num; i++ {
		if num%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	var t, n int
	var p bool

	s := bufio.NewScanner(os.Stdin)
	w := bufio.NewWriter(os.Stdout)

	s.Scan()
	t, _ = strconv.Atoi(s.Text())

	for i := 0; i < t; i++ {
		s.Scan()
		n, _ = strconv.Atoi(s.Text())

		if n == 0 || n == 1 {
			fmt.Fprintln(w, 2)
			continue
		}
		if Prime(n) == true {
			fmt.Fprintln(w, n)
		} else {
			for {
				n++
				p = Prime(n)
				if p == true {
					fmt.Fprintln(w, n)
					break
				}
			}
		}
	}
	w.Flush()
}
