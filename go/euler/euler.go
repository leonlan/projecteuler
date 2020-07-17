package euler

// import "fmt"
import . "math"

func IsPrime(n int) bool {
	if n < 2 {
		return false
	} else if n == 2 {
		return true
	} else if n%2 == 0 {
		return false
	} else {
		for i := 3; i < int(Ceil(Sqrt(float64(n))+1)); i += 2 {
			if n%i == 0 {
				return false
			}
		}
		return true
	}
}

// PrimeFactorization finds the prime factorization of the input number n
// It returns a map of key value pairs where the key is the prime and
// value is the mulitiplicity of that prime
// DOES NOT WORK YET FOR VALUES BELOW 16
func PrimeFactorization(n int) map[int]int {
	var m = make(map[int]int)
	var total = n

	if IsPrime(n) {
		m[n] = 1
		return m
	}

	for total%2 == 0 {
		total = total / 2
		m[2] += 1
	}

	for i := 3; i < int(Ceil(Sqrt(float64(n))+1)); i += 2 {
		if IsPrime(i) && total%i == 0 {
			for total%i == 0 {
				total = total / i
				m[i] += 1
			}
		}
		if total == 1 {
			break
		}
	}
	return m
}

func IsPalindrome(n int) bool {
	// TODO
}
