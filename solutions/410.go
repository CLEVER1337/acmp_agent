package main
import . "fmt"
func main() {
	var (
		q, w, z, x, y    [1e3]int
		n, m, r, v, h, i int
		k                = 1
		P                = Print
	)

	Scan(&n, &m)
	n %= m
	if n < 1 {
		P(0)
		return
	}

	for i := range q {
		q[i] = 1e9
	}

	q[n] = 0
	x[n]--
	for i < h+m {
		w = q
		j := 0
		for j < m {
			l := 0
			for l < 9 {
				l++
				o := (j + l*k) % m
				if w[j]+l < q[o] {
					q[o] = w[j] + l
					z[o] = l
					x[o] = i
					y[o] = j
					h = i
				}
			}
			j++
		}
		k *= 10
		k %= m
		i++
	}

	for r != n {
		i = x[r]
		v = (v*10 + z[r]) % m
		P(z[r])
		k = y[r]
		i--
		for i > x[k] {
			v *= 10 % m
			P(0)
			i--
		}
		r = k
	}
}