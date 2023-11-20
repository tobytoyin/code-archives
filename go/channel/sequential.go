package main

import (
	"fmt"
)

type Queue []int

func Producer(queuePtr *Queue, number int) {
	// produce the number into a Queue
	*queuePtr = append(*queuePtr, number)
}

func Consumer(queuePtr *Queue) {
	// consume a number from the Queue
	queue := *queuePtr
	lastIndex := len(queue) - 1
	consumed := queue[lastIndex]
	fmt.Printf("Consumed: %d\n", consumed)
	*queuePtr = append(queue[lastIndex:], queue[lastIndex+1:]...)
}

func main() {
	items := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	queue := make(Queue, 0)

	for _, item := range items {
		Producer(&queue, item)
		Consumer(&queue)
		fmt.Println(queue)
	}
}
