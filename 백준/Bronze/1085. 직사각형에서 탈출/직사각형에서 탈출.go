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

	var x, y, w, h int
	fmt.Fscanln(reader, &x, &y, &w, &h)

	a := x - 0
	b := y - 0
	c := w - x
	d := h - y

	x_diff := -1

	if a <= c {
		x_diff = a
	} else {
		x_diff = c
	}

	y_diff := -1
	if b <= d {
		y_diff = b
	} else {
		y_diff = d
	}

	if x_diff >= y_diff {
		fmt.Fprint(writer, y_diff)
	} else {
		fmt.Fprint(writer, x_diff)
	}
}