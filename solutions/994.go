package main
import . "fmt"
func main() {
	var (
		p, o             [3e3][3e3]int16
		k, w, v, h, r, j int
		z                = ""
		x                = z
		y                = z
	)

	Scan(&x, &y)
	n := len(x)
	m := len(y)
	i := n - 1
	for i >= 0 {
		j = m - 1
		for j >= 0 {
			if x[i] == y[j] {
				p[i][j] = p[i+1][j+1] + 1
			}
			j--
		}
		i--
	}

	i = n
	for i >= 0 {
		j = m
		for j >= 0 {
			a := p[i][j]
			b := o[i+1][j]
			c := o[i][j+1]
			if c > b {
				b = c
			}
			if a > b {
				b = a
			}
			o[i][j] = b
			j--
		}
		i--
	}

	for r < n {
		j = 0
		for j < m {
			i = 1
			for i <= int(p[r][j]) {
				u := r + i
				t := j + i
				e := int(o[u][t]) + i
				if e > h {
					h, k, w, v = e, r, j, i
				}
				i++
			}
			j++
		}
		r++
	}

	r = k + v
	w += v
	j = int(o[r][w])
	for r <= n-j {
		i = w
		for i <= m-j {
			if int(p[r][i]) >= j {
				z = x[r : r+j]
				goto A
			}
			i++
		}
		r++
	}
A:
	Print(x[k:k+v], `
`, z)
}