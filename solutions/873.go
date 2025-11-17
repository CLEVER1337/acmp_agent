package main
import . "fmt"
func main() {
	n := 0
	m := 0
	Scan(&n, &m)

	n = n * n / 4
	a := 1
	b := 4 % m
	for n > 0 {
		if n&1 > 0 {
			a = a * b % m
		}
		b = b * b % m
		n >>= 1
	}

	Print(a)
}