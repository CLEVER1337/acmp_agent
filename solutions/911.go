package main
import . "fmt"
func main() {
	var (
		c = ""
		l = c
		r = c
		n = 0
		o = 1
		S = Sprint
	)

	Scan(&c, &n)
	for n > 0 {
		b := n % 3
		if b == 1 {
			r += S(o, " ")
		}
		if b > 1 {
			l += S(o, " ")
			n++
		}
		n /= 3
		o *= 3
	}

	if c > "Q" {
		l, r = r, l
	}

	Print("L:", l, `
R:`, r)
}