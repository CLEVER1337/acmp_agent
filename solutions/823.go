package main
import . "fmt"
func A(x int) int {
	if x < 0 {
		x = -x
	}
	return x
}
func main() {
	var (
		d                [51][52]int
		q, g             [51]int
		N                int = 1e6
		n, x, y, z, i, l int
	)

	Scan(&n)
	for i < 51 {
		q[i] = 51
		for j := range d[i] {
			d[i][j] = N
		}
		d[i][1] = i - 1
		i++
	}

	for 0 < n {
		Scan(&x, &y)
		if x < q[y] {
			q[y] = x
		}
		if x > g[y] {
			g[y] = x
		}
		if y > z {
			z = y
		}
		n--
	}

	for n <= z {
		n++
		i = 1
		for i < 51 {
			x = 1
			for x < 51 {
				h := d[x][n-1] + 1
				y = g[n-1]
				if y < 1 {
					h += A(i - x)
				} else {
					a := y
					b := q[n-1]
					y -= b
					p := A(x-a) + y + A(b-i)
					y += A(x-b) + A(a-i)
					if y < p {
						p = y
					}
					h += p
				}
				if h < d[i][n] {
					d[i][n] = h
				}
				x++
			}
			i++
		}
	}

	z++
	for l < 51 {
		if d[l][z] < N {
			N = d[l][z]
		}
		l++
	}

	Print(N - 1)
}