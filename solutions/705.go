package main
import . "fmt"
func main() {
	n := 0
	m := 0
	p := 1

	Scan(&n, &m)
	b := 2 % m
	e := n
	for e > 0 {
		if e&1 > 0 {
			p = p * b % m
		}
		b = b * b % m
		e >>= 1
	}
	n = (p*((n*n-4*n+6)%m) - 6) % m
	if n < 0 {
		n += m
	}

	Print(n)
}