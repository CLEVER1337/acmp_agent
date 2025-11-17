package main
import . "fmt"
func F(i, j, k, l int) int {
	k -= i
	if k < 0 {
		k = -k
	}
	l -= j
	if l < 0 {
		l = -l
	}
	if k+l > 0 {
		if k < 1 {
			k = l
			l = 0
		}
		for l > 0 {
			k, l = l, k%l
		}
	}
	return k + 1
}

func main() {
	var a, b, c, d, e, f int
	Scan(&a, &b, &c, &d, &e, &f)
	Print(F(a, b, c, d) + F(c, d, e, f) + F(e, f, a, b) - 3)
}