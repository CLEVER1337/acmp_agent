package main
import (
	. "fmt"
	. "math"
)
type F = float64
func main() {
	var (
		g, q    [256]F
		e       [27][10][5e3]F
		n, r, l int
		i       = 26
		w       = ""
		u       F
	)

	Scan(&n, &r, &w)
	r--

	for l < n {
		Scan(&q[l])
		l++
	}

	d := 1 << len(w)
	e[26][0][d-1] = 1
	for i >= 0 {
		l = 0
		for l < n {
			z := 0
			for z < d {
				W := e[i][l][z]
				if z < 1 {
					if l == r {
						u += W
					}
				} else if W > 0 {
					var o, f F
					c := 0
					for x, V := range w {
						c = z >> x & 1
						g[V] = F(c)
						o += F(c)
					}
					c = 65
					for c < 91 {
						f += g[c]
						c++
					}
					if i > 0 {
						I := F(i)
						t := Pow(q[l], 1/(o-f+1))
						o = (1-t)*f/I + t*Pow(1-1/I, I-f)
						c = 65
						for c < 91 {
							if g[c] > 0 {
								b := z
								for x, V := range w {
									if V == rune(c) {
										b &^= 1 << x
									}
								}
								e[i-1][l][b] += W * o / f
							}
							c++
						}
						e[i-1][(l+1)%n][z] += (1 - o) * W
					}
				}
				z++
			}
			l++
		}
		i--
	}

	Print(u)
}