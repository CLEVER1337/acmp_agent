package main
import (
	. "fmt"
	. "sort"
)
type V struct{ q, x, y int }
func main() {
	var (
		n, q, l, i int
		x, y       [2e3]int
		z          = make([]V, 0, 100)
	)

	Scan(&n)
	for l < n {
		Scan(&x[l], &y[l])
		l++
	}

	w := make([]V, 0, n-1)
	for i < n {
		w = w[:0]
		l = 0
		for l < n {
			if i != l {
				x := x[l] - x[i]
				y := y[l] - y[i]
				w = append(w, V{x*x + y*y, x, y})
			}
			l++
		}

		Slice(w, func(i, j int) bool {
			a := w[i]
			b := w[j]
			if a.q != b.q {
				return a.q < b.q
			}
			if a.x != b.x {
				return a.x < b.x
			}
			return a.y < b.y
		})

		l = 0
		for l < len(w) {
			r := l
			for r < len(w) && w[r].q == w[l].q {
				r++
			}
			g := w[l:r]
			l = r
			r = len(g)
			r = r * (r - 1) / 2
			z = z[:0]
			for _, v := range g {
				z = append(z, V{0, v.x, v.y})
			}

			o := 0
			for _, v := range z {
				e := V{0, -v.x, -v.y}
				s := 0
				p := len(z)
				h := p
				for s < h {
					f := (s + h) / 2
					if z[f].x < e.x || z[f].x == e.x && z[f].y < e.y {
						s = f + 1
					} else {
						h = f
					}
				}
				m := 0
				for s < p {
					if z[s].x > e.x || z[s].x == e.x && z[s].y > e.y {
						break
					}
					if z[s] == e {
						m++
					}
					s++
				}
				o += m
			}
			q += r - o/2
		}
		i++
	}

	Print(q)
}