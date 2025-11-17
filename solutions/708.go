package main

import . "fmt"

type A [100]int
type T [100]A

func main() {
	var (
		g             T
		n, m, q, w, i int
	)

	Scan(&n, &m)
	for i < n {
		j := 0
		for j < m {
			Scan(&g[i][j])
			j++
		}
		i++
	}

	for {
		var (
			d, y                   T
			o, r                   A
			x, j, h, f, a, c, z, t int
		)

		for j < m {
			i = g[0][j]
			if i >= z {
				z = i
				x = j
			}
			j++
		}
		r[0] = x
		i = 1
		for i < n {
			e := 0
			b := 0
			j = -1
			for j < 2 {
				u := x + j
				if u >= 0 && u < m {
					v := g[i][u]
					if v >= e {
						e = v
						b = u
					}
				}
				j++
			}
			r[i] = b
			x = b
			i++
		}

		for i, j := range r[:n] {
			q += g[i][j]
			g[i][j] = 0
		}

		for f < n {
			j = 0
			for j < m {
				if g[f][j] > 0 {
					h = 1
				}
				j++
			}
			f++
		}
		if h < 1 {
			break
		}

		for a < m {
			d[0][a] = g[0][a]
			a++
		}

		i = 1
		for i < n {
			j = 0
			for j < m {
				a = -1
				for a < 2 {
					f = j + a
					if f >= 0 && f < m {
						h = d[i-1][f] + g[i][j]
						if h >= d[i][j] {
							d[i][j] = h
							y[i][j] = f
						}
					}
					a++
				}
				j++
			}
			i++
		}

		for c < m {
			h = d[n-1][c]
			if h >= t {
				t = h
				a = c
			}
			c++
		}

		i = n
		for i > 0 {
			i--
			o[i] = a
			a = y[i][a]
		}

		for i, j := range o[:n] {
			w += g[i][j]
			g[i][j] = 0
		}
	}

	Print(q, w)
}