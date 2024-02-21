package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {

	var n int
	fmt.Scan(&n)

	count := 0
	now := 666
	for {

		tmp := strconv.Itoa(now)

		if strings.Contains(tmp, "666") {
			count += 1
		}

		if count == n {
			break
		}

		now += 1
	}

	fmt.Println(now)

}