package badgoroutine

import (
	"fmt"
	"time"
)

type Queue []int

func Consumer(queuePtr *Queue) {

	// consume a number from the Queue
	queue := *queuePtr
	lastIndex := len(queue) - 1

	// consider that the coroutine might fail
	// when go Consumer runs before Producers created number
	if lastIndex < 0 {
		return
	}

	consumed := queue[lastIndex]
	*queuePtr = append(queue[:lastIndex], queue[lastIndex+1:]...)

	fmt.Printf("Consumed: %d\n", consumed)
	time.Sleep(1 * time.Second) // assume it takes 1 second to process
}

func DequeueGoroutine() {
	queue := Queue{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	queueCount := len(queue)

	// while loop when the queue is not empty
	for queueCount > 0 {
		go Consumer(&queue)
		queueCount = len(queue)
		fmt.Println(queue)
	}
	// timeout for 10s
	time.Sleep(10 * time.Second)
	fmt.Println("Queue is completed!")
}
