package main
import (
	. "container/list"
	. "fmt"
)

type T struct{ a, b, c, d, e, f int }
type A [2e3]int

var (
	q                      [16]A
	p                      A
	d                      [1e4]T
	m, n, k, h, j, i, u, I int
)

func F(A, B, C int) {
	d[I] = T{A, B, 0, 1, -C, p[A]}
	p[A] = I
	I++
	d[I] = T{B, A, 0, 0, C, p[B]}
	p[B] = I
	I++
}

func main() {
	Scan(&m, &n, &k)
	for j < m {
		u = 0
		for u < n {
			Scan(&q[j][u])
			u++
		}
		j++
	}

	s := m * n

	for i := range p {
		p[i]--
	}

	for i < m {
		j = 0
		for j < n {
			u = i*n + j
			if (i+j)&1 < 1 {
				F(s, u, 0)
				d := 0
				for d < 4 {
					v := i + (1-d&1*2)*(1-d/2)
					o := j + d - d&1*d - d/2
					if v >= 0 && v < m && o >= 0 && o < n {
						F(u, v*n+o, q[i][j]*q[v][o])
					}
					d++
				}
			} else {
				F(u, s+1, 0)
			}
			j++
		}
		i++
	}

	for 0 < k {
		var (
			y, f, r A
			x       List
		)
		for i := range y {
			y[i] = 1e9
		}
		y[s] = 0
		x.PushBack(s)
		for x.Len() > 0 {
			u = x.Remove(x.Front()).(int)
			f[u] = 0
			j = p[u]
			for j > -1 {
				b := &d[j]
				if b.c < b.d {
					i = b.b
					m = y[u] + b.e
					if m < y[i] {
						y[i] = m
						r[i] = j
						if f[i] < 1 {
							x.PushBack(i)
							f[i] = 1
						}
					}
				}
				j = d[j].f
			}
		}
		j = s + 1
		for j != s {
			i = r[j]
			d[i].c++
			d[i^1].c--
			h += d[i].e
			j = d[i].a
		}
		k--
	}

	Print(-h)
}