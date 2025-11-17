package main
import (
	. "fmt"
	. "math"
)

type P struct{ x, y float64 }

func M(o, a, b P) float64 {
	return (a.x-o.x)*(b.y-o.y) - (a.y-o.y)*(b.x-o.x)
}

func main() {
	var (
		Q          = 1e-9
		m          = 0.
		N, i, l, r int
		F          func(int)
		h          [10]P
		d          [10][]P
		g          [10][]int
		S          = Scan
		A          = Abs
	)

	S(&N)
	for i < N {
		k := 0
		S(&k)
		d[i] = make([]P, k)
		j := 0
		for j < k {
			S(&d[i][j].x, &d[i][j].y)
			j++
		}
		h[i] = d[i][k-1]
		i++
	}

	for l < N {
		i = 0
		for i < N {
			for _, p := range d[i] {
				if A(h[l].x-p.x) < Q && A(h[l].y-p.y) < Q {
					g[i] = append(g[i], l)
					break
				}
			}
			i++
		}
		l++
	}

	for r < N {
		var (
			o, u       []P
			t          = map[any]int{}
			z          [10]bool
			i, l, j, k int
			a          = 0.
		)

		F = func(u int) {
			if !z[u] {
				z[u] = 1 > 0
				for _, v := range g[u] {
					F(v)
				}
			}
		}
		F(r)

		for j < N {
			if z[j] {
				for _, p := range d[j] {
					k := P{p.x, p.y}
					if t[k] < 1 {
						t[k] = 1
						o = append(o, p)
					}
				}
			}
			j++
		}

		n := len(o)
		for l < n {
			j = l + 1
			for j < n {
				if o[l].x > o[j].x+Q || A(o[l].x-o[j].x) < Q && o[l].y > o[j].y+Q {
					o[l], o[j] = o[j], o[l]
				}
				j++
			}
			l++
		}

		for i < n {
			for len(u) > 1 {
				j = len(u) - 1
				if M(u[j-1], u[j], o[i]) > -Q {
					break
				}
				u = u[:j]
			}
			u = append(u, o[i])
			i++
		}

		l = len(u)
		i = n - 2
		for i >= 0 {
			for len(u) > l {
				j = len(u) - 1
				if M(u[j-1], u[j], o[i]) > -Q {
					break
				}
				u = u[:j]
			}
			if i > 0 {
				u = append(u, o[i])
			}
			i--
		}

		i = len(u)
		for k < i {
			j = k
			k++
			a += u[j].x*u[k%i].y - u[j].y*u[k%i].x
		}

		a = A(a) / 2
		if a > m {
			m = a
		}
		r++
	}

	Print(m)
}