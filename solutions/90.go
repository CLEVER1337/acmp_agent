package main
import . "fmt"
func main() {
	var x, y, i, k, r, c, q, w, e, t, o int
	s := ""

	Scan(&x, &y, &k)
	for i < k {
		i++
		Scan(&c, &q, &w, &e, &t, &o)
		a := (w-c)*(y-q) - (e-q)*(x-c)
		e = (t-w)*(y-e) - (o-e)*(x-w)
		c = (c-t)*(y-o) - (q-o)*(x-t)
		if (a > 0 && e > 0 && c > 0) ||
			(a < 0 && e < 0 && c < 0) {
			r++
			s += Sprint(" ", i)
		}
	}

	Print(r, s)
}