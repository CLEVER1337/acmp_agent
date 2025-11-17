package main
import . "fmt"
func main() {
	var (
		g, p          [103][103]int
		n, k, x, l, o int
	)

	Scan(&n, &k)
	for l < n {
		j := 0
		for j < n {
			Scan(&g[l][j])
			p[l][j] = -1
			j++
		}
		l++
	}

	u := p
	p[0][0] = g[0][0]
	for 1 < k {
		l = 0
		for l < n {
			j := 0
			for j < n {
				d := 0
				for d < 4 {
					f := l + d%2 - d/3*2
					z := j + 1 - d + d/3*2
					if f >= 0 && z >= 0 && p[f][z] > 0 {
						e := p[f][z] + g[l][j]
						if e > u[l][j] {
							u[l][j] = e
						}
					}
					d++
				}
				j++
			}
			l++
		}
		p = u
		k--
	}

	for o < n {
		k = 0
		for k < n {
			l = p[o][k]
			if l > x {
				x = l
			}
			k++
		}
		o++
	}

	Print(x)
}