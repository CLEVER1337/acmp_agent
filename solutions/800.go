package main
import . "fmt"
type T [800]int
var (
	q                   T
	g, o                [800]T
	n, z, h, i, l, k, I int
	d                   = 1
)

func F(a, p, c int) {
	if c < 1 {
		h++
		return
	}
	u := a + 1
	for u < I && p*g[c][u] <= n {
		if o[a][u] == 1 {
			F(u, p*q[u], c-1)
		}
		u++
	}
}

func main() {
	Scan(&n, &z)
	for d <= n/d {
		if n%d < 1 {
			q[I] = d
			I++
		}
		d++
	}
	j := I
	for j > 0 {
		j--
		d = q[j]
		if d*d < n {
			q[I] = n / d
			I++
		}
	}

	for i < I {
		j = i
		for j < I {
			d = q[i]
			y := q[j]
			for y > 0 {
				d, y = y, d%y
			}
			o[i][j] = d
			o[j][i] = d
			j++
		}
		g[1][i] = q[i]
		i++
	}

	for k < z {
		k++
		d = 0
		for d < I {
			i = n + 1
			if k == 1 {
				i = q[d]
			} else if d != I {
				i = g[k-1][d+1] * q[d]
			}
			g[k][d] = i
			d++
		}
	}

	for l < I {
		F(l, q[l], z-1)
		l++
	}

	Print(h)
}