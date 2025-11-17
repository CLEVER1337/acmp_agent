package main
import . "fmt"
func main() {
	var (
		n, x, y, l int
		a          = -1 << 19
		b          = a
		c          = a * -3
	)

	Scan(&n)
	for 0 < n {
		Scan(&x, &y, &l)
		if a < x {
			a = x
		}
		if b < y {
			b = y
		}
		x += y + l
		if c > x {
			c = x
		}
		n--
	}
	c -= a + b
	s := float64(c*c) / 2
	if c < 0 {
		s = 0
	}

	Print(s)
}