package main

import "fmt"
import "math"

func main() {
	total := 0
	a, b := 1, 2
	for ; b <= 4 * int(math.Pow10(6)); {
		if b % 2 == 0 {
			total += b
		}
		a, b = b, a+b
	}
	fmt.Println(total)
}
