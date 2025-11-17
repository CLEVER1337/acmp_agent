package main
import (
	. "fmt"
	. "math"
)
func main() {
	var (
		n, i, f int
		c       = 0.
		p       = c
		e       = c
		s       = "NO"
		a, b    [2e3]float64
	)

	Scan(&n, &c, &p)
	for f <= n {
		Scan(&a[f], &b[f])
		f++
	}

	for i < n {
		f = 0
		t := 0.
		for f <= n {
			if f != i {
				t += Hypot(a[i]-a[f], b[i]-b[f])
			}
			f++
		}

		if t < e || i < 1 {
			e = t
		}
		i++
	}

	if e*c <= p {
		s = "YES"
	}

	Print(s)
}