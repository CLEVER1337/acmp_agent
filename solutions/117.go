package main
import (
	. "fmt"
	. "math"
	. "sort"
)
type F = float64
type P struct{ x, y int }
func main() {
	var (
		p, q                      []P
		X                         = -1.
		Y                         F
		n, x, y, z, a, i, l, s, h int
		H                         = Hypot
	)

	Scan(&n)
	for i < n {
		Scan(&x, &y)
		p = append(p, P{x, y})
		i++
	}

	Slice(p, func(i, j int) bool {
		if p[i].y != p[j].y {
			return p[i].y < p[j].y
		}
		return p[i].x < p[j].x
	})

	for s < 1 || z > 0 {
		q = append(q, p[z])
		s = 1
		o := -2.
		i = 0
		for i < n {
			r := F(p[i].x - p[z].x)
			t := F(p[i].y - p[z].y)
			k := H(r, t)
			e := X*r/k + Y*t/k
			if e > o {
				h = i
				o = e
			}
			i++
		}
		X = F(p[h].x - p[z].x)
		Y = F(p[h].y - p[z].y)
		o = H(X, Y)
		X /= o
		Y /= o
		z = h
	}

	q = append(q, q[0])
	for l < len(q)-1 {
		f := q[l+1]
		a += (f.x - q[l].x) * (f.y + q[l].y)
		l++
	}

	a++
	Print(a / 2)
}