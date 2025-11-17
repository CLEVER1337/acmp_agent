package main
import (
	. "fmt"
	. "math"
)
func main() {
	r := 0.
	n := r
	c := 0

	Scan(&r, &n)
	m := int(r / n)
	i := -m - 1
	for i <= m {
		b := float64(i) * n
		a := Abs(b)
		b += n
		if b > a {
			a = b
		}
		c += int(Sqrt(r*r-a*a)/n) * 2
		i++
	}

	Print(c)
}