package main
import (
	. "fmt"
	. "math"
	. "sort"
)
type I = int
type F = float64
type M struct {
	s    F
	a, b I
}

func main() {
	var (
		a, b, c    [100]F
		q          [][]I
		w          = []F{0, 1}
		t          []F
		K          = 1e-12
		n, z, j, i I
		S          = Slice
	)

	Scan(&n)
	for j < n {
		Scan(&a[j], &b[j], &c[j])
		j++
	}

	for i < n {
		j = i + 1
		for j < n {
			A := a[i] - a[j]
			B := b[i] - b[j]
			C := c[i] - c[j]
			if A == 0 {
				x := -C / B
				if x > K && x < 1-K {
					w = append(w, x)
				}
			}
			C = Sqrt(B*B - 4*A*C)
			u := (-B - C) / 2 / A
			A = (-B + C) / 2 / A
			C = 0
			for C < 2 {
				if u > K && u < 1-K {
					w = append(w, u)
				}
				u = A
				C++
			}
			j++
		}
		i++
	}
	Float64s(w)
	i = 1
	for i < len(w) {
		if w[i]-w[z] > K {
			z++
			w[z] = w[i]
		}
		i++
	}
	w = w[:z+1]
	i = 1
	for i < len(w) {
		u := (w[i] + w[i-1]) / 2
		if u > K && u < 1+K {
			t = append(t, u)
		}
		t = append(t, w[i])
		i++
	}
	w = t
	s := make([]M, n)
	for _, p := range w {
		i = 0
		for i < n {
			s[i] = M{c[i] + b[i]*p + a[i]*p*p, i, 0}
			i++
		}
		S(s, func(i, j I) bool {
			u := s[i].s - s[j].s
			if Abs(u) < K {
				return s[i].a < s[j].a
			}
			return u > 0
		})
		i = 1
		for i < n {
			s[i].b = s[i-1].b
			if s[i-1].s-s[i].s > K {
				s[i].b = i + 1
			}
			i++
		}
		S(s, func(i, j I) bool {
			return s[i].a < s[j].a
		})
		u := make([]I, n)
		i = 0
		for i < n {
			u[i] = s[i].b
			i++
		}
		q = append(q, u)
	}
	S(q, func(i, j I) bool {
		for k := range q[i] {
			u := q[j][k]
			l := q[i][k]
			if l != u {
				return l < u
			}
		}
		return 1 < 0
	})
	j = 1
	i = 1
	for i < len(q) {
		for I := range q[i] {
			if q[i][I] != q[i-1][I] {
				j++
				break
			}
		}
		i++
	}

	Print(j)
}