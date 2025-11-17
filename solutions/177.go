package main
import (
	. "fmt"
	. "sort"
)
type I = int
func main() {
	var (
		q                      []I
		w, z, x                [101]I
		a, b, c, d, i, j, B, C I
		m                      = map[I]I{}
		n                      = map[I]I{}
		S                      = Scan
		P                      = Printf
		W                      = `put cargo %d to cell %d
`
	)

	S(&a, &b)
	for i < a {
		i++
		S(&w[i])
	}

	for j < b {
		j++
		S(&z[j], &c, &d)
		m[c] = 1
		n[c] = j
		m[d] = 2
		n[d] = j
	}

	for t := range m {
		q = append(q, t)
	}
	Ints(q)
	for _, v := range q {
		c = m[v]
		d = n[v]
		if c > 1 {
			e := x[d]
			if e > 0 {
				w[e] += z[d]
				P(`take cargo %d from cell %d
`, d, e)
				x[d] = 0
			}
		}
		if c < 2 {
			A := 0
			c = 9e9
			i = 0
			for i < a {
				i++
				if w[i] >= z[d] && w[i] < c {
					c = w[i]
					A = i
				}
			}
			if A > 0 {
				P(W, d, A)
				w[A] -= z[d]
				x[d] = A
			} else {
				A = 9e9
				c = 0
				for c < b {
					c++
					j = x[c]
					i = 0
					for i < a {
						i++
						if i != j && w[i] > z[c] && w[j]+z[c] > z[d] && z[c] < A {
							A = z[c]
							B = c
							C = i
						}
					}
				}
				if A == 9e9 {
					P(`cargo %d cannot be stored
`, d)
				} else {
					i = B
					j = x[i]
					c = C
					w[j] += z[i]
					w[c] -= z[i]
					x[i] = c
					w[j] -= z[d]
					x[d] = j
					P(`move cargo %d from cell %d to cell %d
`+W, i, j, c, d, j)
				}
			}
		}
	}
}