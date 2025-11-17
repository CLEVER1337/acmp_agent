package main
import . "fmt"
type I = int
type E struct{ a, b I }
var (
	z, q, w, g       []I
	o                [1e5]I
	h                [2e5][]E
	u, n, d, m, c, x I
	i                = 1
)

func F(r, p I) I {
	x := 1
	for i := range h[r] {
		v := &h[r][i]
		if v.a != p {
			r := F(v.a, r)
			o[-v.b-1] = n - r
			v.b = r
			x += r
		}
	}
	return x
}

func G(r, p, k I) {
	if k == 1 {
		for _, e := range h[r] {
			if e.a != p {
				x++
			}
		}
		return
	}
	for _, e := range h[r] {
		if e.a != p {
			G(e.a, r, k-1)
		}
	}
}

func main() {
	Scan(&n, &d)
	if d&1 < 1 {
		for i < n {
			Scan(&m, &c)
			h[m] = append(h[m], E{c, -i})
			h[c] = append(h[c], E{m, -i})
			o[i]--
			i++
		}
		d /= 2
		if d == 1 {
			i = 0
			for u < n {
				u++
				m = len(h[u])
				i += m * (m - 1) * (m - 2) / 6
			}
			u = i
			goto A
		}
		F(1, 0)
		for 0 < n {
			n--
			for i := range h[n] {
				v := &h[n][i]
				if v.b < 0 {
					v.b = o[-v.b-1]
				}
			}
			m = 0
			for _, v := range h[n] {
				if v.b >= d {
					m++
				}
			}
			if m > 2 {
				z = nil
				for _, v := range h[n] {
					if v.b >= d {
						x = 0
						G(v.a, n, d-1)
						z = append(z, x)
					}
				}
				c = len(z)
				q = make([]I, c)
				w = make([]I, c)
				g = make([]I, c)
				c--
				q[c] = z[c]
				i = c
				for i > 0 {
					i--
					q[i] = q[i+1] + z[i]
				}
				i = c
				for i > 0 {
					i--
					w[i] = w[i+1] + z[i]*q[i+1]
				}
				i = c
				for i > 0 {
					i--
					g[i] = g[i+1] + z[i]*w[i+1]
				}
				u += g[0]
			}
		}
	}
A:
	Print(u)
}