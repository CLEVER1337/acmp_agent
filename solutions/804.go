package main

import (
	. "fmt"
	. "strings"
)

var n, m, v, h, o, i, j, u, k int

type A []byte
type B []int

func F(q B, g []A, z *int) []A {
	for len(q) > 0 {
		h = q[0]
		o = q[1]
		j = q[2]
		q = q[3:]
		if h == n-2 && o == m-2 {
			*z = j
		}
		j++
		for _, v := range []B{{-1, 0}, {1, 0}, {0, -1}, {0, 1}} {
			a, b := h+v[0], o+v[1]
			if g[a][b] == 46 {
				g[a][b] = 42
				q = append(q, a, b, j)
			}
		}
	}
	return g
}
func main() {
	s := ""
	Scan(&n, &m)
	g := make([]A, n)
	for i < n {
		Scan(&s)
		g[i] = A(s)
		j = Index(s, "T")
		if j > 0 {
			h = i
			o = j
		}
		i++
	}

	q := B{h, o, 0}
	g[h][o] = 42

	g = F(q, g, &v)

	if g[n-2][m-2] == 46 {
		k = 1
	}

	i = 1
	for i < n-1 {
		j = 1
		for j < m-1 {
			if g[i][j] != 35 {
				g[i][j] = 46
			}
			j++
		}
		i++
	}

	q = B{1, 1, 0}
	g[1][1] = 42

	g = F(q, g, &u)

	s = "No"
	Println(u)
	if u < v || k > 0 {
		s = "Yes"
	}
	Print(s)
}