package main
import (
	. "fmt"
	. "math"
	. "sort"
)

type A struct {
	a int
	b float64
}

func main() {
	var (
		g                [1e5]A
		n, e, f, o, i, j int
		q                = 0.
		h                = q
		z                = ""
	)

	Scan(&n)
	for j < n {
		Scan(&z)
		for j, c := range z {
			if c > 57 {
				Sscan(z[:j], &h)
				z = z[j+1:]
				break
			}
		}
		switch z {
		case "m":
			h *= 1e3
		case "ile":
			h *= 1609
		case "in":
			h *= 33
		case "airi":
			h *= 1852
		case "hang":
			h *= 3
		case "en":
			h *= 38
		}
		g[j] = A{j + 1, h}
		j++
	}

	Slice(g[:n], func(i, j int) bool {
		return g[i].b > g[j].b
	})

	if n > 200 {
		n = 200
	}

	for i < n {
		j = i
		for j < n {
			j++
			k := j
			for k < n {
				k++
				a := g[i].b
				b := g[j].b
				c := g[k].b
				p := (a + b + c) / 2
				u := p * (p - a) * (p - b) * (p - c)
				if u > q {
					q = u
					e = g[i].a
					f = g[j].a
					o = g[k].a
				}
			}
		}
		i++
	}

	Print(Sqrt(q)/4, e, f, o)
}