package main
import . "fmt"
type R struct{ a, b, c, d int }
type A [101]int
func main() {
	var (
		d             A
		w             [25]A
		n, m, j, l, i int
	)

	Scan(&n)
	s := make([]R, n)
	for j < n {
		Scan(&s[j].a, &s[j].b, &s[j].c, &s[j].d)
		j++
	}

	for l < n {
		j = l + 1
		for j < n {
			a := s[l]
			b := s[j]
			y := a.a
			if b.a > y {
				y = b.a
			}
			x := a.c
			if b.c < x {
				x = b.c
			}
			z := a.b
			if b.b > z {
				z = b.b
			}
			c := a.d
			if b.d < c {
				c = b.d
			}
			if y < x && z < c ||
				y == x && z < c ||
				z == c && y < x {
				w[l][j] = 1
				w[j][l] = 1
			}
			j++
		}
		l++
	}

	for i < n {
		if d[i] < 1 {
			var o []int
			q := []int{i}
			d[i] = 1
			for len(q) > 0 {
				j = len(q) - 1
				l = q[j]
				q = q[:j]
				o = append(o, l)
				j = 0
				for j < n {
					if w[l][j] > d[j] {
						d[j] = 1
						q = append(q, j)
					}
					j++
				}
			}
			g := [101]A{}
			for _, i := range o {
				r := s[i]
				j = r.a
				for j < r.c {
					l = r.b
					for l < r.d {
						if j < 101 && l < 101 {
							g[j][l] = 1
						}
						l++
					}
					j++
				}
			}
			j = 0
			l = 0
			for l < 101 {
				y := 0
				for y < 101 {
					j += g[l][y]
					y++
				}
				l++
			}
			if j > m {
				m = j
			}
		}
		i++
	}

	Print(m)
}