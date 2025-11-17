package main
import . "fmt"
func main() {
	var n, m, s, i int
	a := 1

	Scan(&n, &m)
	for i < n {
		i++
		a = a * 2 * i % m
		s += a
		s %= m
	}

	Print(s)
}