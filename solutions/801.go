package main
import (
	. "fmt"
	. "math"
)

type T = float64
type L struct{ a, b, c T }

var (
	W             = 1e9
	q             []L
	n, o, e, h, u T
	z             = -W
	w             = W
)

func F(f, y T) T {
	m := 0.
	for _, v := range q {
		s := Abs(v.a*f + v.b*y + v.c)
		if s > m {
			m = s
		}
	}
	return m
}

func G(X, Y, A T) T {
	for A-Y > 1e-6 {
		n = (Y*6 + A*5) / 11
		e = (Y*5 + A*6) / 11
		if F(X, n) < F(X, e) {
			A = e
		} else {
			Y = n
		}
	}
	return (A + Y) / 2
}

func main() {
	Scan(&n)
	for 0 < n {
		Scan(&o, &e, &h, &u)
		x := e*h - o*u
		u -= e
		o -= h
		e = Hypot(u, o)
		q = append(q, L{u / e, o / e, x / e})
		n--
	}

	for w-z > 1e-6 {
		h = (z*6 + w*5) / 11
		u = (z*5 + w*6) / 11
		if F(h, G(h, -W, W)) < F(u, G(u, -W, W)) {
			w = u
		} else {
			z = h
		}
	}

	z += w
	Print(z/2, G(z/2, -W, W))
}