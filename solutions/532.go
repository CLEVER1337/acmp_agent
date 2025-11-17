package main
import (
	B "bufio"
	. "fmt"
	. "os"
)

type I = int
type M struct{ a, b I }
type T []I
type H struct {
	a T
	b []M
	f func(i, j I) bool
}

func (h *H) P(x I) {
	h.a = append(h.a, x)
	x = len(h.a) - 1
	for {
		i := (x - 1) / 2
		if !h.f(h.a[x], h.a[i]) {
			break
		}
		h.V(i, x)
		x = i
	}
}

func (h *H) Q() I {
	n := len(h.a) - 1
	h.V(0, n)
	i := 0
	for {
		k := 2*i + 1
		if k >= n {
			break
		}
		j := k
		k++
		if k < n && h.f(h.a[k], h.a[k-1]) {
			j = k
		}
		h.V(i, j)
		i = j
	}
	i = h.a[n]
	h.a = h.a[:n]
	return i
}

func (h *H) V(i, j I) {
	h.a[i], h.a[j] = h.a[j], h.a[i]
}

func main() {
	var (
		z, e                               []M
		u, o, p, k, x, y, a, b, c, d, j, i I
		R                                  = B.NewReader(Stdin)
	)

	Scan(&u, &o, &p)
	for 0 < u {
		Fscan(R, &a, &b, &c, &d)
		k += b * (d - c)
		if a > b {
			z = append(z, M{a - b, 2})
			e = append(e, M{c, d})
		}
		u--
	}

	b = p + 2
	q := make(T, b)
	w := make(T, b)
	s := make(T, b)
	t := make(T, b)
	for i < len(z) {
		q[e[i].a]++
		w[e[i].b]++
		i++
	}
	i = 1
	for i < b {
		s[i] = s[i-1] + q[i-1]
		t[i] = t[i-1] + w[i-1]
		i++
	}

	L := make(T, s[b-1]+q[b-1])
	W := make(T, t[b-1]+w[b-1])
	for i := range q {
		q[i] = 0
		w[i] = 0
	}

	for u < len(z) {
		i = e[u].a
		c = e[u].b
		L[s[i]+q[i]] = u
		W[t[c]+w[c]] = u
		q[i]++
		w[c]++
		u++
	}

	g := &H{T{}, z, func(i, j I) bool { return z[i].a > z[j].a }}
	h := &H{T{}, z, func(i, j I) bool { return z[i].a < z[j].a }}
	for j < p {
		j++
		a = t[j]
		c = t[j] + w[j]
		for a < c {
			d = W[a]
			if z[d].b < 1 {
				x -= z[d].a
				y--
			}
			z[d].b = 2
			a++
		}
		a = s[j]
		c = a + q[j]
		for a < c {
			d = L[a]
			g.P(d)
			z[d].b = 1
			a++
		}
		for y < o && len(g.a) > 0 {
			d = g.Q()
			if z[d].b < 2 {
				z[d].b = 0
				h.P(d)
				y++
				x += z[d].a
			}
		}
		if len(h.a)*len(g.a) > 0 {
			d = h.a[0]
			a = g.a[0]
			for z[d].b > 1 {
				h.Q()
				d = h.a[0]
			}
			for z[a].b > 1 {
				g.Q()
				a = g.a[0]
			}
			if z[d].a < z[a].a {
				c = h.Q()
				b = g.Q()
				x -= z[c].a
				x += z[b].a
				h.P(b)
				g.P(c)
				z[b].b = 0
				z[c].b = 1
			}
		}
		k += x
	}

	Print(k)
}