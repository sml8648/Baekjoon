package main

import (
	"bufio"
	"fmt"
	"os"
)

// Queue represents a basic FIFO queue.
type Queue struct {
	items []interface{}
}

// Enqueue adds an element to the end of the queue.
func (q *Queue) Enqueue(item interface{}) {
	q.items = append(q.items, item)
}

// Dequeue removes and returns the first element from the queue.
func (q *Queue) Dequeue() interface{} {
	if len(q.items) == 0 {
		return nil
	}
	item := q.items[0]
	q.items = q.items[1:]
	return item
}

// Peek returns the first element from the queue without removing it.
func (q *Queue) Peek() interface{} {
	if len(q.items) == 0 {
		return nil
	}
	return q.items[0]
}

// IsEmpty checks if the queue is empty.
func (q *Queue) IsEmpty() bool {
	return len(q.items) == 0
}

// Size returns the number of elements in the queue.
func (q *Queue) Size() int {
	return len(q.items)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	queue := Queue{}

	var n, k int
	fmt.Fscan(reader, &n, &k)

	for i := 1; i <= n; i++ {
		queue.Enqueue(i)
	}

	var result []interface{}
	for {
		for i := 0; i < k; i++ {
			if i == (k - 1) {
				t := queue.Dequeue()
				result = append(result, t)
			} else {
				t := queue.Dequeue()
				queue.Enqueue(t)
			}
		}

		if len(result) == n {
			break
		}
	}

	fmt.Fprint(writer, "<")
	for i := 0; i < n; i++ {
		fmt.Fprint(writer, result[i])
		if i == n-1 {
			continue
		}
		fmt.Fprint(writer, ", ")
	}
	fmt.Fprint(writer, ">")

}