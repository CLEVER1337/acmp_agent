package main
import . "fmt"
func main() {
	var n, d, m, i int

	Scan(&n, &d)
	e := 2
	if d == n {
		m = 1
		e = n + 1
	}
	n -= d
	for i*i < n {
		i++
		c := i
		j := 0
		for j < 2 {
			t := n + d
			u := 0
			for c > 1 && t%c == d {
				t /= c
				u++
			}
			if u > m {
				m = u
				e = c
			}
			c = n / i
			j++
		}
	}

	Print(e, m)
}