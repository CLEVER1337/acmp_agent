package main
import (
	. "fmt"
	. "sort"
)
type I = int
type R struct{ a, b, c, d I }

func F(x, y I) {
	if d[x][y] < 1 {
		d[x][y] = 1
		i := 0
		for i < 4 {
			V := i - i/3*2
			m := x + V - 1
			t := y + V - i/2*2
			if m >= 0 && m < u && t >= 0 && t < p {
				for i, V := range o[x][y] {
					if V != o[m][t][i] {
						goto A
					}
				}
				F(m, t)
			A:
			}
			i++
		}
	}
}

var (
	h                   []R
	o                   [199][][100]bool
	d                   [200][200]I
	n                   = 10001
	q                   = []I{-n, n}
	w                   = q
	i, j, l, x, y, u, p I
	k                   = 2
	S                   = SearchInts
)

func main() {
	Scan(&n)
	for i < n {
		Scan(&x, &y, &u, &p)
		if x > u {
			x, u = u, x
		}
		if y > p {
			y, p = p, y
		}
		h = append(h, R{x, y, u, p})
		q = append(q, x, u)
		w = append(w, y, p)
		i++
	}

	for k > 0 {
		w, q = q, w
		u, p = p, u
		Ints(w)
		x = 1
		i = 1
		for i < len(w) {
			if w[i] != w[i-1] {
				w[x] = w[i]
				x++
			}
			i++
		}
		w = w[:x]
		p = len(w) - 1
		k--
	}

	for i := range h {
		r := &h[i]
		r.a = S(q, r.a)
		r.c = S(q, r.c)
		r.b = S(w, r.b)
		r.d = S(w, r.d)
	}

	for x := range o {
		o[x] = make([][100]bool, len(w)-1)
	}

	for j < n {
		r := h[j]
		x = r.a
		for x < r.c {
			y = r.b
			for y < r.d {
				o[x][y][j] = 1 > 0
				y++
			}
			x++
		}
		j++
	}

	for l < u {
		i = 0
		for i < p {
			if d[l][i] < 1 {
				k++
				F(l, i)
			}
			i++
		}
		l++
	}

	Print(k)
}