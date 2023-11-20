package channel

import (
	"fmt"
	"time"
)

type Queue []int

func processing() {
	// assume it takes 1 second to process
	time.Sleep(1 * time.Second)
}

func Consumer(queue chan int) {
	consumed := <-queue
	fmt.Printf("Consumed: %d\n\n", consumed)
	processing()
}

func Producer(queue chan int, item int) {
	fmt.Printf("Produced: %d\n", item)
	queue <- item
}

func DequeueChannel() {
	queue := Queue{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	queueCh := make(chan int)

	for _, item := range queue {
		go Producer(queueCh, item)
		go Consumer(queueCh)
	}
	// timeout after 10s
	time.Sleep(10 * time.Second)
	fmt.Println("Queue is completed!")
}
