package main
import . "fmt"

func F(n, m int) int {
	if n-m > m {
		m = n - m
	}
	c := 1
	i := n
	for i > m {
		c *= i
		i--
	}
	n -= m
	for n > 1 {
		c /= n
		n--
	}
	return c
}

func main() {
	var (
		W             [10]int
		N, g, f, u, i int
		d             = 1
	)

	Scan(&N)
	if N > 1 {
		W[0] = 1
		for d < N {
			W[d] = 10 * W[d-1]
			d++
		}
		for i < N {
			u += W[i]
			i++
		}
		for {
			d = 0
			c := 1
			i = u
			for i > 0 {
				a := i % 10
				d += a
				c *= a
				i /= 10
			}

			if d == c {
				if f < 1 {
					f = u
				}
				c = 1
				i = 1
				d = 1
				for d < N {
					if u/W[d]%10 == u/W[d-1]%10 {
						i++
					} else {
						c *= F(d, i)
						i = 1
					}
					d++
				}
				c *= F(d, i)
				g += c
			}
			d = 0
			for u%10 == 9 {
				u /= 10
				d++
			}
			if u < 1 {
				break
			}
			u++
			q := u % 10
			for d > 0 {
				u = u*10 + q
				d--
			}
		}
	} else {
		g = 10
	}

	Print(g, f)
}