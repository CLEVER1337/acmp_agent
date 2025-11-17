package main
import (
	. "fmt"
	. "math"
	. "sort"
)
type T = float64
type I = int
type G struct{ A, B X }
type H struct {
	t    T
	x, y I
}
type X []H

func F(g G) T {
	m := 0.
	for _, v := range g.B {
		m += T(v.y)
	}
	return m / T(len(g.A))
}

func main() {
	var (
		A, B, w    X
		R          = 1e-9
		h, a, i, j I
		o, t       T
		S          = Scan
		L          = Slice
		P          = Println
	)

	S(&h)
	for i < h {
		i++
		S(&o)
		A = append(A, H{o, i, 0})
	}

	S(&h)
	for j < h {
		j++
		S(&a)
		B = append(B, H{0, j, a})
	}

	L(A, func(i, j I) bool {
		return A[i].t > A[j].t
	})

	L(B, func(i, j I) bool {
		return B[i].y > B[j].y
	})

	for len(B) > len(A) {
		B = B[:len(B)-1]
	}
	for len(B) < len(A) {
		B = append(B, H{})
	}

	q := []G{{X{A[0]}, X{B[0]}}}
	i = 1
	for i < len(A) {
		h = len(q) - 1
		Z := &q[h]
		if Z.A[0].t-A[i].t < R {
			Z.A = append(Z.A, A[i])
			Z.B = append(Z.B, B[i])
		} else {
			q = append(q, G{X{A[i]}, X{B[i]}})
		}
		i++
	}

	for len(q) > 0 {
		o = 9e9
		i = 0
		h = len(q) - 1
		for i < h {
			t := (q[i].A[0].t - q[i+1].A[0].t) / (F(q[i]) - F(q[i+1]))
			if t < o {
				o = t
			}
			i++
		}
		k := F(q[h])
		if k > 0 {
			t := q[h].A[0].t / k
			if t < o {
				o = t
			}
		}
		for _, x := range q {
			k = t
			i = 0
			a = len(x.B)
			for i < a {
				j = 0
				for j < len(x.A) {
					B := x.B[(i+j)%a]
					w = append(w, H{k + o/T(a)*T(i), x.A[j].x, B.x})
					x.A[j].t -= o / T(a) * T(B.y)
					j++
				}
				i++
			}
		}
		t += o
		g := []G{q[0]}
		h = 0
		for i, x := range q {
			if i > 0 {
				if Abs(x.A[0].t-q[i-1].A[0].t) < R {
					for _, o := range x.A {
						g[h].A = append(g[h].A, o)
					}
					for _, c := range x.B {
						g[h].B = append(g[h].B, c)
					}
				} else {
					g = append(g, x)
					h++
				}
			}
		}
		q = g
		h = len(q) - 1
		for h > -1 && q[h].A[0].t < R {
			q = q[:h]
			h--
		}
	}

	L(w, func(i, j I) bool {
		return w[i].t < w[j].t
	})

	P(t)
	for _, v := range w {
		if v.y > 0 {
			P(v.t, v.x, v.y)
		}
	}
}