package main
import . "fmt"

var (
	q       [8][8]int
	d, z, g [8]int
	n, l, k int
	w       = -1
)

func F(x int) {
	i := 0
	if x == n {
		u := 0
		for i < n {
			j := 0
			for j < n {
				if j != g[i] {
					u += q[i][j]
				}
				j++
			}
			i++
		}
		if w == -1 || u < w {
			w = u
			z = g
		}
		return
	}
	for i < n {
		if d[i] < 1 {
			d[i] = 1
			g[x] = i
			F(x + 1)
			d[i] = 0
		}
		i++
	}
}

func main() {
	Scan(&n)
	for l < n {
		j := 0
		for j < n {
			Scan(&q[l][j])
			j++
		}
		l++
	}

	F(0)
	for k < n {
		Printf("%c", 65+z[k])
		k++
	}

	Print(`
`, w)
}