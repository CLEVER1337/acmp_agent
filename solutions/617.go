package main
import (
	. "fmt"
	. "math/big"
)

var (
	m, n, w, b, r, c, i, j, l int64
	N                         = NewInt
	a                         = N(0)
)

func F(g, k int64) *Int {
	r := N(1)
	l = 0
	for l < k {
		r.Div(r.Mul(r, N(g-l)), N(l+1))
		l++
	}
	return r
}

func main() {
	Scan(&m, &n, &w, &b)
	for r < m {
		r++
		c = 0
		for c < n {
			c++
			q := N(0)
			i = 0
			for i < r {
				j = 0
				for j < c {
					t := N(1)
					t.Mul(t.Mul(t.Mul(t, F(r, i)), F(c, j)), F((r-i)*(c-j), w))
					if (i+j)&1 > 0 {
						q.Sub(q, t)
					} else {
						q.Add(q, t)
					}
					j++
				}
				i++
			}
			a.Add(a, q.Mul(q.Mul(q.Mul(q, F(m, r)), F(n, c)), F((m-r)*(n-c), b)))
		}
	}

	Print(a)
}