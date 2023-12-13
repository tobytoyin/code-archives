package main

import (
	"bufio"
	"os"
)

func ReadLog(path string) <-chan string {
	logStream := make(chan string)

	file, err := os.Open(path)
	if err != nil {
		return logStream
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		logStream <- scanner.Text()
	}

	return logStream
}


"{{time}} {{value}} {{priority}}"
