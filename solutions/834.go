package main
import (
	. "fmt"
	. "math"
)
func main() {
	var x, y, z, v, r float64

	Scan(&x, &y, &z, &v, &r)
	x -= z
	y -= v
	z = Hypot(x, y)
	y = Pi * r * r
	v = Sqrt(z*z - r*r)
	x = 360
	if z > r {
		y = y/x*(x-Asin(v/z)*x/Pi) + v*r
	}

	Print(y)
}