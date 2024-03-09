package main

import (
	"bufio"
	"fmt"
	"os"
)

type Node struct {
	value interface{}
	next  *Node
}

type Queue struct {
	front *Node
	rear  *Node
	size  int
}

func (q *Queue) Enqueue(value interface{}) {
	newNode := &Node{value, nil}
	if q.rear == nil {
		q.front = newNode
		q.rear = newNode
	} else {
		q.rear.next = newNode
		q.rear = newNode
	}
	q.size++
}

func (q *Queue) Dequeue() interface{} {
	if q.front == nil {
		return nil
	}
	value := q.front.value
	q.front = q.front.next
	if q.front == nil {
		q.rear = nil
	}
	q.size--
	return value
}

func (q *Queue) Peek() interface{} {
	if q.front == nil {
		return nil
	}
	return q.front.value
}

func (q *Queue) IsEmpty() bool {
	return q.size == 0
}

func (q *Queue) Size() int {
	return q.size
}

func main() {

	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n int
	fmt.Fscan(reader, &n)
	queue := Queue{}

	for i := 1; i <= n; i++ {
		queue.Enqueue(i)
	}

	for {
		if queue.Size() == 1 {
			break
		}

		queue.Dequeue()
		tmp := queue.Dequeue()
		queue.Enqueue(tmp)
	}

	fmt.Fprint(writer, queue.Peek())
}