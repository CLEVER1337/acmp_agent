package main
import (
	. "fmt"
	. "math"
)
func main() {
	a := 0.
	b := a
	c := a

	Scan(&a, &b, &c)
	x := a
	if b < x {
		x = b
	}
	if c < x {
		x = c
	}

	z := a
	if b > z {
		z = b
	}
	if c > z {
		z = c
	}

	y := a + b + c - x - z
	x = (z*z + y*y - x*x) / 2 / z / y
	c = y * y * Sqrt(1/(x*x)-1)
	if y > z*x {
		c = z * z * x * Sqrt(1-x*x)
	}
	if x < .7 {
		c = z * z / 2
	}

	Print(c / 2)
}