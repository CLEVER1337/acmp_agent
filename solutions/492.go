package main
import . "fmt"
func main() {
	var x, y, a, b, v, t, d int
	s := "NO"

	Scan(&x, &y, &a, &b, &v, &t, &d)
	x += a * t
	y += b * t
	a = x*x + y*y
	v *= t
	t = d - v
	v += d
	q := d*d > a
	if q && (t < 0 || a >= t*t) ||
		!q && a <= v*v {
		s = "YES"
	}

	Print(s)
}