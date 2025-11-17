package main
import (
	. "fmt"
	. "math"
)

type A struct{ x, y float64 }
type B []int

func main() {
	var (
		p    [2e3]A
		g    B
		n, j int
		l    = 0.
		r    = 2e4
		P    = Println
	)

	Scan(&n)
	for j < n {
		Scan(&p[j].x, &p[j].y)
		j++
	}

	for r-l > 1e-10 {
		m := (l + r) / 2
		c := make(B, n)
		i := 0
		for i < n {
			if c[i] < 1 {
				c[i] = 1
				s := B{i}
				j = 1
				for j > 0 {
					j--
					u := s[j]
					s = s[:j]
					v := 0
					for v < n {
						if v != u && Hypot(p[u].x-p[v].x, p[u].y-p[v].y) < 2*m {
							if c[v] < 1 {
								c[v] = 3 - c[u]
								s = append(s, v)
								j++
							}
							if c[v] == c[u] {
								r = m
								goto A
							}
						}
						v++
					}
				}
			}
			i++
		}
		l = m
		g = c
	A:
	}

	P(l)
	for _, c := range g {
		P(c)
	}
}