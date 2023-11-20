We have an `Queue` object to store the values

By Dequeue the `Queue` sequentially, we run the following: 

```shell
go test -v ./sequential -count=1
```

We would be able to dequeue the last item for each loop as expected but each time the `Consumer` would pause for 1 second to wait for the process to complete. This would in total take about 10s. 

By Dequeue using a incorrect Goroutine (concurrency approach): 

```shell
go test -v ./bad_goroutine -count=1
```

We would be able to dequeue it much faster with about just 1s. This is because the 1s non-thread blocking process time allow the other goroutines to process something else from the `Queue`. However, this create another problem. 

Because gorotuines are able to spawn whenever the main thread is not blocked, during that 1s window, it spawn many coroutnie to dequeue the last item from the Queue, even when the prior `Consumer` already picked up that item. This causing the `Queue` element to be processed for multiple. 

