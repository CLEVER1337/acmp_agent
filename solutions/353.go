package main
import (
	. "fmt"
	. "math"
	. "sort"
)
func main() {
	var (
		d    [1e5]float64
		n, i int
		m    = 0.
		f    = "%.f"
	)

	Scan(&n)
	for i < n {
		Scan(&d[i])
		i++
	}

	Float64s(d[:n])
	for 2 < n {
		n--
		a := d[n]
		b := d[n-1]
		c := d[n-2]
		s := (a + b + c) / 2
		e := Sqrt(s * (s - a) * (s - b) * (s - c))
		if a+b > c && e > m {
			m = e
		}
	}

	if m > 0 {
		f = "%.3f"
	}

	Printf(f, m)
}