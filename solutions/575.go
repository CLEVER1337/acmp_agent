package main
import . "fmt"
func main() {
	var (
		g          [100][100]int
		n, m, i, l int
		q          = 0.
		w          = q
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

	for l < n {
		j := 0
		for j < m {
			k := g[l]
			i = k[j]
			v := l + 1
			z := j + 1
			if v < n && z < m && (i != g[v][j] || i != k[z] || i != g[v][z]) {
				q++
			}
			if v < n && i != g[v][j] {
				w++
			}
			if z < m && i != k[z] {
				w++
			}
			j++
		}
		l++
	}

	Print(.12*q + .48*w)
}