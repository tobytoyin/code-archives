package goroutine

import (
	"fmt"
	"time"
)

type Queue []int

func processing() {
	// assume it takes 1 second to process
	time.Sleep(1 * time.Second)
}

func Consumer(queuePtr *Queue) {

	// consume a number from the Queue
	queue := *queuePtr
	lastIndex := len(queue) - 1

	// exit when the queue is empty
	if lastIndex < 0 {
		return
	}

	consumed := queue[lastIndex]
	*queuePtr = append(queue[:lastIndex], queue[lastIndex+1:]...)
	processing()
	fmt.Printf("Consumed: %d\n", consumed)
}

func DequeueGoroutine() {
	queue := Queue{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	queueCount := len(queue)

	// while loop when the queue is not empty
	for queueCount > 0 {
		go Consumer(&queue)
		queueCount = len(queue)
	}

	// timeout for 5s
	time.Sleep(5 * time.Second)
	fmt.Println("Queue is completed!")
}
