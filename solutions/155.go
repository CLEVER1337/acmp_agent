package main
import (
	. "fmt"
	. "math/big"
	. "strings"
)

type R struct{ x, y *Int }
var (
	n, i, X int64
	m       = 1
	s       = ""
	r       = s
	N       = NewInt
	P       = Print
	O       = N(1)
)

func H(x, y *Int) R {
	w := N(1).Set(x)
	d := N(1).Set(y)
	g := N(1).GCD(O, O, w, d)
	w.Div(w, g)
	d.Div(d, g)
	return R{w, d}
}

func main() {
	Scan(&n, &s)
	u := Split(s, ".")
	if len(u) > 1 {
		s = u[0]
		r = u[1]
		for len(r) < 4 {
			r += "0"
		}
		O = N(1e4)
	}

	Sscanf(s+r, "%d", &X)
	q := H(N(X), O)
	o := 1 << n
	d := make([][]R, o)
	for i < n {
		Scan(&X)
		d[1<<i] = []R{H(N(X), N(1))}
		i++
	}

	for m < o {
		if len(d[m]) < 1 {
			e := (m - 1) & m
			for e > 0 {
				for _, a := range d[e] {
					for _, b := range d[m^e] {
						c := H(N(1).Add(
							N(1).Mul(a.x, b.y),
							N(1).Mul(b.x, a.y)),
							N(1).Mul(a.y, b.y))
						d[m] = append(d[m], c,
							H(N(1).Mul(N(1).Mul(a.x, b.x), c.y),
								N(1).Mul(N(1).Mul(a.y, b.y), c.x)))
					}
				}
				e--
				e &= m
			}
			u := map[any]int{}
			var t []R
			for _, r := range d[m] {
				k := r.x.String() + "/" + r.y.String()
				if u[k] < 1 {
					u[k] = 1
					t = append(t, r)
				}
			}
			d[m] = t
		}
		for _, r := range d[m] {
			e := N(1).Sub(N(1).Mul(r.x, q.y), N(1).Mul(q.x, r.y))
			e.Mul(e.Abs(e), N(100))
			if e.Cmp(N(1).Mul(r.y, q.y)) < 1 {
				P("YES")
				return
			}
		}
		m++
	}

	P("NO")
}