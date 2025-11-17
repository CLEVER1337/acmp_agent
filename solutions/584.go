package main
import . "fmt"
type T struct{ a, b int }

var (
	s    []int
	u    [3e5]T
	R    = T{12, 0}
	L    = T{6, 0}
	A    = T{0, 1}
	B    = T{0, 2}
	h, w int
	e    = 150000
	p    = e
	P    = Print
)

func main() {
	Scan(&h, &w)
	for h != 1 && w != 1 && w != 2 && h != 2 && w != 3 {
		s = append(s, h)
		h, w = w-2, h
	}

	H := T{0, h}
	W := T{0, w}
	Z := T{0, h - 1}
	if h == 1 || w == 1 {
		for _, v := range []T{H, R, W, R, H, R, W} {
			u[p] = v
			p++
		}
	} else if w == 2 {
		for _, v := range []T{H, R, B, R, A, R, A, L, Z, R, A} {
			u[p] = v
			p++
		}
	} else if h == 2 {
		for _, v := range []T{B, R, W, R, B, R, A, R, A, L, {0, w - 2}, L, A, R, A} {
			u[p] = v
			p++
		}
	} else if w == 3 {
		for _, v := range []T{H, R, {0, 3}, R, H, R, A, R, Z, L, A, L, Z, R, A} {
			u[p] = v
			p++
		}
	}

	w = len(s)
	for w > 0 {
		w--
		u[e].b += 2
		e--
		u[e] = R
		e--
		u[e] = T{0, s[w]}
		u[p-3].b++
		u[p-2] = L
		u[p-1] = T{0, s[w] - 1}
		u[p] = R
		u[p+1] = A
		p += 2
	}

	P(p - e)
	for e < p {
		A = u[e]
		Printf(`
%c `, A.a+102)
		if A.b > 0 {
			P(A.b)
		}
		e++
	}
}