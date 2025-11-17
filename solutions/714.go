package main
import (
	. "fmt"
	. "math"
)

type T struct{ a, b, c float64 }

func G(a, b T) float64 {
	return Hypot(a.a-b.a, a.b-b.b)
}

func F(a, b, c T) T {
	var (
		A T
		e = b.a - a.a
		f = b.b - a.b
		g = c.a - a.a
		h = c.b - a.b
		i = e*e + f*f
		j = g*g + h*h
		d = e*h - g*f
	)

	if Abs(d) > 0 {
		A = T{(i*h-j*f)/d/2 + a.a, (e*j-g*i)/d/2 + a.b, 0}
	}

	return A
}

func Q(a, b T) (T, T) {
	return T{(a.a + b.a) / 2, (a.b + b.b) / 2, 0}, T{a.b - b.b, b.a - a.a, 0}
}

func main() {
	var (
		p    [4]T
		o    []T
		i, j int
		P    = Print
	)

	for j < 4 {
		Scan(&p[j].a, &p[j].b)
		j++
	}

	w := F(p[0], p[1], p[2])
	if Abs(G(w, p[3])-G(w, p[0])) < 1e-5 {
		P(`Infinity
`, w.a, w.b, 0)
		return
	}

	for i < 4 {
		var (
			h    [3]T
			d, j int
		)
		for j < 4 {
			if j != i {
				h[d] = p[j]
				d++
			}
			j++
		}
		w = F(h[0], h[1], h[2])
		if w.a != 0 {
			o = append(o, T{w.a, w.b, (G(w, h[0]) + G(w, p[i])) / 2})
		}
		if i < 3 {
			var (
				c    = p[2-i+i/2]
				z, k = Q(p[0], p[i+1])
				j, u = Q(c, p[3-i/2])
				q    = k.a*u.b - k.b*u.a
				t    = ((j.a-z.a)*u.b - (j.b-z.b)*u.a) / q
				v    = T{z.a + t*k.a, z.b + t*k.b, 0}
			)
			if Abs(q) > 1e-5 {
				o = append(o, T{v.a, v.b, (G(v, p[0]) + G(v, c)) / 2})
			}
		}
		i++
	}

	m := o[0]
	for _, v := range o {
		if v.c < m.c {
			m = v
		}
	}

	P(len(o), `
`, m.a, m.b, m.c)
}