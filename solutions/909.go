package main
import . "fmt"
func main() {
	var (
		g                   [1e3][]byte
		n, m, w, a, b, l, i int
		z                   = ""
	)

	Scan(&n, &m)
	for l < n {
		Scan(&z)
		g[l] = []byte(z)
		l++
	}

	for i < n {
		j := 0
		for j < m {
			e := g[i][j]
			if e > 82 {
				q := [][]int{{i, j}}
				u := 0
				o := 1
				if e < 84 {
					u++
					o--
				}
				for len(q) > 0 {
					p := q[0]
					q = q[1:]
					l = 0
					for l < 4 {
						c := p[0] + l - l&1*l - l/2
						k := p[1] + (1-l&1*2)*(1-l/2)
						if c >= 0 && c < n && k >= 0 && k < m {
							f := &g[c][k]
							if *f > 82 {
								o++
								if *f < 84 {
									u++
									o--
								}
								*f = 0
								q = append(q, []int{c, k})
							}
						}
						l++
					}
				}
				if u > 0 && o < 1 {
					w++
				}
				if o > 0 && u < 1 {
					b++
				}
				if u*o > 0 {
					a++
				}
			}
			j++
		}
		i++
	}

	Print(w, a, b)
}