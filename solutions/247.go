package main
import . "fmt"
type T [101]int
func main() {
	var (
		d, q, h       [101]T
		p             T
		n, c, b, i, k int
	)
	for i, v := range d {
		for j := range v {
			d[i][j] = 1e9
		}
	}
	d[0][0] = 0

	Scan(&n)
	for i < n {
		Scan(&p[i])
		j := 0
		for j < 101 {
			s := d[i][j]
			if s < 1e9 {
				x := j
				if p[i] > 100 {
					x++
				}
				z := i + 1
				d[z][x] = s + p[i]
				q[z][x] = j
				if j > 0 {
					x = j - 1
					if s < d[z][x] {
						d[z][x] = s
						q[z][x] = j
						h[z][x] = 1
					}
				}
			}
			j++
		}
		i++
	}

	i = 1e9
	for k < 101 {
		if d[n][k] <= i {
			i = d[n][k]
			b = k
		}
		k++
	}

	k = b
	for n > 0 {
		c += h[n][k]
		k = q[n][k]
		n--
	}

	Print(i, b, c)
}