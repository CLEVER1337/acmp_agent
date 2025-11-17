package main
import . "fmt"
func main() {
	var (
		q, w, z, h    [123]int
		a             [2e5]int
		n, i, y, x, c int
	)

	Scan(&n)
	for i < n {
		Scanf("%c", &c)
		if c > 32 {
			a[i] = c
			a[i+n] = c
			i++
		}
	}

	g := n / 2
	o := n - 1
	m := g
	i = y
	for i < g {
		q[a[i]]++
		z[a[i]] += g - i
		i++
	}
	i = g
	for i < o {
		i++
		w[a[i]]++
		h[a[i]] += i - g
	}

	for o+1 < 2*n {
		if y < g {
			q[a[y]]--
			z[a[y]] -= g - y
			q[a[g]]++
		}
		o++
		y++
		if o > g {
			c = a[g+1]
			w[c]--
			h[c]--
			w[a[o]]++
			h[a[o]] += o - g
		}
		g++
		e := 0
		c = 97
		for c < 123 {
			z[c] += q[c]
			h[c] -= w[c]
			i = c - a[g]
			if i < 0 {
				i = -i
			}
			e += (z[c] + h[c]) * i
			c++
		}
		if e > x {
			m = g
			x = e
		}
	}

	Print(x, `
`, m%n+1)
}