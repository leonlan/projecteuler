package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func readLines(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

func main() {
	var total int64
	lines, err := readLines("../data/p013.txt")
	if err != nil {
		log.Fatalf("readLines: %s", err)
	}
	for _, line := range lines {
		n, err := strconv.ParseInt(line[:13], 10, 64)
		if err != nil {
			log.Fatalf("strconv: %s", err)
		}
		total += n
	}
	ans := strconv.FormatInt(total, 10)[:10]
	fmt.Println(ans)
}
