package main
import . "fmt"
type T [2]int
func main() {
	var (
		g, p [1e5 + 1]T
		y    []int
		n    = 0
		h    = 2
		r    = 1
		s    = ""
		m    = T{0, 1}
		P    = Print
	)

	Scan(&n, &s)
	for h <= n {
		var w T
		q := 0
		for q < 2 {
			z := 0
			for z < 2 {
				r := s[2*q+z] & 1
				o := m[q] + z
				if o > w[r] {
					w[r] = o
					g[h][r] = z
					p[h][r] = q
				}
				z++
			}
			q++
		}
		m = w
		h++
	}

	for n > 1 {
		y = append(y, g[n][r])
		r = p[n][r]
		n--
	}
	y = append(y, r)
	n = len(y)
  
	if m[1] < 1 {
		P("No solution")
		n = 0
	}
	for n > 0 {
		n--
		P(y[n])
	}
}