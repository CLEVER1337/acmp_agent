package main
import . "fmt"
func main() {
	var (
		n, d, i, f int
		P          = Print
		S          = Sprint
	)

	Scan(&n, &d)
	P(n, "=")
	s := S(n/d) + "."
	n %= d
	for i < 3*d {
		n *= 10
		s += S(n / d)
		n %= d
		i++
	}

	i = 57
	for i > 48 {
		x := ""
		n = 1
		for _, v := range s {
			r := "0"
			if int(v) < i {
				if v < 47 {
					r = "."
				}
			} else {
				r = S(d)
				n = 0
			}
			x += r
		}
		if n < 1 {
			w := -1
			i := d
			n = len(x)
			for i > 0 {
				if x[n-d:] == x[n-d-i:n-i] {
					w = i
				}
				i--
			}
			n--
			for x[n-w] == x[n] {
				x = x[:n]
				n--
			}
			for x[0] == 48 && x[1] > 46 {
				x = x[1:]
				n--
			}
			if w == 1 && x[n] == 48 {
				x = x[:n]
				n--
				if x[n] < 47 {
					x = x[:n]
					n--
				}
			} else {
				n += 1 - w
				x = x[:n] + "(" + x[n:] + ")"
			}
			if f > 0 {
				P("+")
			}
			P(x)
			f = 1
		}
		i--
	}
}