package main
import . "fmt"
var P = Print
func F(r, m int, c []int) {
	for m <= r {
		F(r-m, m, append(c, m))
		m++
	}
	m = len(c) - 1 - 1e9*r
	if m > 0 {
		for i, v := range c {
			P(v)
			if i < m {
				P("+")
			}
		}
		P("\r\n")
	}
}
func main() {
	n := 0
	Scan(&n)
	F(n, 1, nil)
}