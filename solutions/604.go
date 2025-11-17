package main
import (
	. "fmt"
	. "math/big"
)

type I = Int
type U = int

var (
	b       [200][200]U
	c       [200]*I
	a, g, m U
	N       = NewInt
)

func F(x, y, f U) *I {
	var (
		t I
		l U
		p = N(1)
		r = N(0)
	)
	for l < 2 {
		j := 0
		if f > 0 {
			r.Set(p)
		}
		for j < a {
			if j != y && b[x][j] > 0 {
				if l < 1 {
					p.Mul(p, H(j, x))
				} else {
					r.Add(r, t.Mul(N(0).Div(p, H(j, x)), F(j, x, 1)))
				}
			}
			j++
		}
		l++
	}

	return r
}

func H(x, y U) *I {
	if c[x] == nil {
		var (
			q, h, u []*I
			j       U
			t, r    I
			p       = N(1)
		)
		for j < a {
			if j != y && b[x][j] > 0 {
				X := H(j, x)
				q = append(q, X)
				p.Mul(p, X)
				h = append(h, F(j, x, 1))
				u = append(u, F(j, x, 0))
			}
			j++
		}
		r.Set(p)

		for i, v := range q {
			r.Add(&r, t.Mul(N(0).Div(p, v), u[i]))
			j = i + 1
			for j < len(q) {
				w := N(0).Div(p, v)
				r.Add(&r, N(0).Mul(t.Mul(w.Div(w, q[j]), h[i]), h[j]))
				j++
			}
			i++
		}
		c[x] = &r
	}

	return c[x]
}

func main() {
	Scan(&a)
	i := a

	for 1 < i {
		Scan(&g, &m)
		g--
		m--
		b[g][m] = 1
		b[m][g] = 1
		i--
	}

	Print(H(0, -1))
}