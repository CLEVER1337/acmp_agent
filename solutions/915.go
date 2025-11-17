package main
import . "fmt"
func M(a, b int) int {
	if a > b {
		b = a
	}
	return b
}

func main() {
	var (
		q, z, g    [1e5]int
		n, m, a, i int
		Q          = -1 << 30
	)

	Scan(&n, &m)
	for i < m {
		i++
		q[i] = Q
		z[i] = Q
		g[i] = Q
	}
	for 0 < n {
		i = 0
		for i < m {
			Scan(&a)
			y := 1
			x := 2
			c := 3
			if a > 0 {
				y = 6
				x = 5
				c = 4
			}
			u := i - 1
			if u < 0 {
				u = m
			}
			y = y*a + M(q[u], q[i])
			x = x*a + M(z[u], z[i])
			c = c*a + M(g[u], g[i])
			q[i] = M(x, c)
			z[i] = M(c, y)
			g[i] = M(y, x)
			i++
		}
		n--
	}

	m--
	Print(M(q[m], M(z[m], g[m])))
}