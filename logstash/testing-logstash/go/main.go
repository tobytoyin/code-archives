package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
	"time"
)

// actual reading, converts input stream to a channel
func readFileLines(path string, lines chan string) {
	file, _ := os.Open(path)
	defer file.Close()

	s := bufio.NewScanner(file)
	for s.Scan() {
		lines <- s.Text()
	}
}

func ReadLog(path string, networkSend func(string)) {
	file, _ := os.Open(path)
	defer file.Close()

	logStream := make(chan string)    // input stream
	go readFileLines(path, logStream) // go and read
	for log := range logStream {
		time.Sleep(1 * time.Second)
		fmt.Println(log)

		networkSend(log)

	}
}

func SendTCP(log string) {
	arguments := os.Args
	if len(arguments) == 1 {
		fmt.Println("Please provide host:port.")
		return
	}

	CONNECT := arguments[1]
	conn, err := net.Dial("tcp", CONNECT)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Fprintf(conn, log+"\n")
}

func main() {

	path := "/Users/tobiasto/Projects/code-archives/logstash/testing-logstash/logs/syslogs.log"
	go ReadLog(path, SendTCP)

	time.Sleep(5 * time.Second)
}
