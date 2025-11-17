package main
import (
	. "fmt"
	. "math"
)
func main() {
	var x, y, a, b float64
	s := "Imp"

	Scan(&x, &y, &a, &b)
	if x < y {
		x, y = y, x
	}
	if a < b {
		a, b = b, a
	}

	d := (x*x + y*y) / 4
	v := a/2 - Sqrt(d-b*b/4)
	d = b/2 - Sqrt(d-a*a/4)
	if x <= a && y <= b || v*v+d*d >= y*y {
		s = "P"
	}

	Print(s + "ossible")
}