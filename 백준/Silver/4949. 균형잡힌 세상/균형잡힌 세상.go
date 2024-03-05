package main

import (
	"bufio"
	"fmt"
	"os"
)

type Stack struct {
	data []rune
}

func (s *Stack) Push(x rune) {
	s.data = append(s.data, x)
}

func (s *Stack) Pop() rune {
	if len(s.data) == 0 {
		return -1
	}
	x := s.data[len(s.data)-1]
	s.data = s.data[:len(s.data)-1]
	return x
}

// func (s *Stack) Size() int {
// 	return len(s.data)
// }

func (s *Stack) IsEmpty() int {
	if len(s.data) == 0 {
		return 1
	}
	return 0
}

func (s *Stack) Top() rune {
	if len(s.data) == 0 {
		return -1
	}
	return s.data[len(s.data)-1]
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	for {
		s, _ := reader.ReadString('\n')

		stack := Stack{}
		result := "yes"

		if s[0] == 46 {
			break
		}

		for _, char := range s {
			if char == 40 || char == 91 {
				stack.Push(char)
			} else if char == 41 {
				top := stack.Top()
				if top == 40 {
					stack.Pop()
				} else {
					result = "no"
					break
				}
			} else if char == 93 {
				top := stack.Top()
				if top == 91 {
					stack.Pop()
				} else {
					result = "no"
					break
				}
			}
		}

		if stack.Top() != -1 {
			result = "no"
		}

		fmt.Fprintln(writer, result)

	}
}
