package main

import (
	"bufio"
	"fmt"
	"os"
)

type Stack struct {
	data []int
}

func (s *Stack) Push(x int) {
	s.data = append(s.data, x)
}

func (s *Stack) Pop() int {
	if len(s.data) == 0 {
		return -1
	}
	x := s.data[len(s.data)-1]
	s.data = s.data[:len(s.data)-1]
	return x
}

func (s *Stack) Size() int {
	return len(s.data)
}

func (s *Stack) IsEmpty() int {
	if len(s.data) == 0 {
		return 1
	}
	return 0
}

func (s *Stack) Top() int {
	if len(s.data) == 0 {
		return -1
	}
	return s.data[len(s.data)-1]
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var N int
	fmt.Fscan(reader, &N)

	stack := Stack{}

	for i := 0; i < N; i++ {

		var n int
		fmt.Fscan(reader, &n)

		if n == 0 {
			stack.Pop()
		} else {
			stack.Push(n)
		}
	}

	sum := 0
	for _, num := range stack.data {
		sum += num
	}

	fmt.Fprint(writer, sum)
}