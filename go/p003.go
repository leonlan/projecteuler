package main

import "fmt"
import . "./euler"

func max(numbers map[int]int) int {
	var maxNumber int
	for n := range numbers {
		maxNumber = n
		break
	}
	for n := range numbers {
		if n > maxNumber {
			maxNumber = n
		}
	}
	return maxNumber
}

func main() {
	pf := PrimeFactorization(600851475143)
	fmt.Println(max(pf))
}
