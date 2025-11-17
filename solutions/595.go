package main
import . "fmt"
type T struct {
	h, p [6e4]int
	c    int
}

func G(s string) *T {
	var (
		h, p [6e4]int
		m    int = 1e9 + 7
		i        = 0
	)
	p[0] = 1
	for i < len(s) {
		i++
		h[i] = (h[i-1]*131 + int(s[i-1])) % m
		p[i] = p[i-1] * 131 % m
	}
	return &T{h, p, m}
}

func F(q *T, l, r int) int {
	return (q.h[r] - q.h[l]*q.p[r-l]%q.c + q.c) % q.c
}

func main() {
	s := ""
	t := s
	i := 0
	P := Print

	Scan(&s, &t)
	n := len(s)
	if n == len(t) {
		x := G(s)
		y := G(t)
		b := []byte(t)
		w := len(b)
		for i < w {
			w--
			b[i], b[w] = b[w], b[i]
			i++
		}
		z := G(string(b))
		i = 0
		for i < n {
			if F(x, i, n) == F(y, 0, n-i) && F(x, 0, i) == F(z, 0, i) {
				P(`Yes
`, i)
				return
			}
			i++
		}
	}

	P("No")
}