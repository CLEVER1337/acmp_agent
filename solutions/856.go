package main
import (
	. "fmt"
	. "math"
)

var (
	w, n, o, k, y, b, a, i, x float64
	U                         = 1e3
	m                         = 0
	W                         bool
)

func F() {
	z := a*x - b*i + b*y - a*k
	q := Hypot(a, b)
	W = z*z/(q*q) > w*w
}

func main() {
	Scan(&w, &n, &o, &k, &y, &b, &a)
	w += o
	k *= U
	y *= U
	b *= U
	a *= U
	o = -n - 1
	p := n + 1
	for i < U*n {
		for {
			x = o * U
			F()
			if W {
				break
			}
			o--
		}
		for {
			x = o * U
			F()
			if b*(i-y) <= a*(x-k) || !W {
				break
			}
			o++
		}
		for {
			x = p * U
			F()
			if W {
				break
			}
			p++
		}
		for {
			x = (p - 1) * U
			F()
			if b*(i-y) >= a*(x-k) || !W {
				break
			}
			p--
		}
		h := int(o)
		g := int(p - 1)
		s := int(i / U)
		h += s&1 ^ h&1
		g -= s&1 ^ g&1
		if s < g {
			g = s
		}
		if -s > h {
			h = -s
		}
		if h <= g {
			m += (g-h)/2 + 1
		}
		i += U
	}

	Print(m)
}