package main
import . "fmt"
func main() {
	var b, a, n int

	Scan(&n)
	for n&1 < 1 {
		n /= 2
		a++
	}
	for n%5 < 1 {
		n /= 5
		b++
	}

	if a > b {
		b = a
	}

	a = 1
	k := 10 % n
	for k > 1 {
		k = k * 10 % n
		a++
	}

	Print(b, a)
}