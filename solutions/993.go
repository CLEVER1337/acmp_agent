package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
func main() {
	var (
		a, q          [2e5 + 1]int
		n, k, D, j, g int
		z             = 1
		r             = b.NewReader(Stdin)
	)

	Scan(&n, &k)
	for j < n {
		Fscan(r, &a[j])
		j++
		if z <= n {
			z *= 2
		}
	}

	o := make([]int, 2*z)

	for g < n {
		i := a[g]
		q[i]++
		y := i + z
		o[y] = q[i]
		for y > 1 {
			y /= 2
			h := o[2*y]
			m := o[2*y+1]
			if h < m {
				m = h
			}
			o[y] = m
		}
		if i > 0 {
			l := z
			r := i - 1 + z
			u := 9 << 18
			for l <= r {
				if l&1 > 0 {
					if o[l] < u {
						u = o[l]
					}
					l++
				}
				if r&1 < 1 {
					if o[r] < u {
						u = o[r]
					}
					r--
				}
				l /= 2
				r /= 2
			}
			j = q[i] - u
			if j > D {
				D = j
			}
		}
		if D > k {
			n = g
		}
		g++
	}

	Print(n)
}