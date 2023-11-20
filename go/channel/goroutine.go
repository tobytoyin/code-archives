package main

import (
	"fmt"
	"time"
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

	// consider that the coroutine might fail
	// when go Consumer runs before Producers created number
	if lastIndex < 0 {
		fmt.Println("No item in the queue")
		return
	}

	consumed := queue[lastIndex]
	fmt.Printf("Consumed: %d\n", consumed)
	*queuePtr = append(queue[lastIndex:], queue[:lastIndex]...)
}

func main() {
	// items := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	// queue := make(Queue, 0)

	// for _, item := range items {
	// 	// using the same piece of code but run in async-await mode
	// 	// our queue is now completely messed up
	// 	// this is because goroutine causing the data become out of sync
	// 	go Producer(&queue, item)
	// 	go Consumer(&queue)
	// 	fmt.Println(queue)
	// }

	queue := Queue{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	queueCount := len(queue)

	for queueCount > 0 {
		go Consumer(&queue)
		fmt.Println(queue)

		time.Sleep(1 * time.Second)
		fmt.Println(queueCount)
		queueCount = len(*&queue)
	}

}
