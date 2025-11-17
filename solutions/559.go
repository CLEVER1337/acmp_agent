package main
import (
	. "fmt"
	. "math"
)
func main() {
	var d, r, n, i float64

	Scan(&d, &r, &n)
	P := Pi * r * r
	R := 2 * r
	D := R*d + P

	for i < n-1 {
		i++
		l := 0.
		v := d + R
		for v-l > 1e-8 {
			z := (l + v) / 2
			a := .5*P + R*(z-r)
			x := z - d - r
			if z < r {
				x = r - z
			}
			x = 2 * Acos(x/r)
			x = .5 * r * r * (x - Sin(x))
			if z < r {
				a = x
			}
			if z > d+r {
				a = D - x
			}
			if a < i*D/n {
				l = z
			} else {
				v = z
			}
		}
		Println(l)
	}
}