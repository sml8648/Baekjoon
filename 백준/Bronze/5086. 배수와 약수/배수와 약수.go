package main

import "fmt"

func main() {

	for {
		var a int
		var b int
		fmt.Scan(&a, &b)

		if a == 0 && b == 0 {
			break
		}

		if b%a == 0 {
			fmt.Println("factor")
			continue
		} else if a%b == 0 {
			fmt.Println("multiple")
			continue
		} else {
			fmt.Println("neither")
			continue
		}
	}

}