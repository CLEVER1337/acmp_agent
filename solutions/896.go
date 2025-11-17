package main
import . "fmt"
func main() {
	n := 0
	m := 0

	Scan(&n, &m)
	p := n + m
	for n > 0 {
		m, n = n, m%n
	}

	Print(p - m)
}