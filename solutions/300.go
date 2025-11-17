package main
import (
	. "fmt"
	. "sort"
)

type M struct{ a, b, c int }

func L(a, b M) bool { return a.a*b.b <= b.a*a.b }
func A(i int) M     { return M{q[i].b*q[i].c + x, q[i].c, 0} }

var (
	q                   [4]M
	p, x, h, d, v, y, i int
	j                   = 1
	e                   = M{0, 1, 0}
	P                   = Print
)

func main() {
	for p < 4 {
		Scan(&d, &v)
		q[p] = M{p, d, v}
		p++
	}

	Scan(&p, &x)
	for j < 4 {
		if L(A(j), A(y)) {
			y = j
		}
		j++
	}

	Slice(q[:], func(i, j int) bool {
		return L(A(i), A(j))
	})

	for i < 4 {
		j = i
		z := A(i)
		for j < 4 && L(A(j), z) {
			j++
		}
		if j > i+1 {
			v = i
			for v < j {
				d = y - q[v].a
				if d < 0 {
					d = -d
				}
				if d > 4-d {
					d = 4 - d
				}
				if L(M{e.a + d*p*e.b, e.b, 0}, z) {
					h++
					goto A
				}
				v++
			}
		}
		d = y - q[i].a
		if d < 0 {
			d = -d
		}
		if d > 4-d {
			d = 4 - d
		}
		if !L(M{e.a + d*p*e.b, e.b, 0}, z) {
			break
		}
		h++
		y = q[i].a
		e = z
		i = j
	}
A:
	if h == 4 {
		P("ALIVE")
		return
	}
	P(h)
}