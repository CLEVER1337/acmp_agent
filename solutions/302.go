package main
import (
	. "fmt"
	. "math"
)
func main() {
	var (
		x, y, d, c [2e3]float64
		n, i       int
		e          = .0
	)

	Scan(&n)
	for i < n {
		Scan(&x[i], &y[i])
		i++
		d[i] = 9e9
	}

	for {
		m := 9e9
		r := -1
		i = 0
		for i < n {
			if c[i] < 1 && d[i] < m {
				m = d[i]
				r = i
			}
			i++
		}

		if r < 0 {
			break
		}

		e = Max(e, d[r])
		c[r] = 1
		i = 0
		for i < n {
			if c[i] < 1 {
				a := x[i] - x[r]
				m = y[i] - y[r]
				d[i] = Min(a*a+m*m, d[i])
			}
			i++
		}
	}

	Printf("%.2f", Sqrt(e))
}