package main
import . "fmt"
type H [2]int
type T [2e5 + 2]int
func main() {
	var (
		w                = 13
		z                = 131
		o                = 7
		d                = 9
		k, g, x, m, y, c T
		q, i, l, I, j, u int
		a                = ""
		b                = a
		h                = map[H]int{}
	)
	o += 1e9

	k[0] = 1
	g[0] = 1
	for i < 2e5 {
		i++
		k[i] = k[i-1] * w % o
		g[i] = g[i-1] * z % d
	}

	Scan(&a, &b)
	A := len(a)
	B := len(b)
	if B <= A {
		for l < A {
			m[l+1] = (m[l]*w + int(a[l])) % o
			x[l+1] = (x[l]*z + int(a[l])) % d
			l++
		}
		b += b
		for j < len(b) {
			y[j+1] = (y[j]*w + int(b[j])) % o
			c[j+1] = (c[j]*z + int(b[j])) % d
			j++
		}
		for I < B {
			h[H{(y[I+B] - y[I]*k[B]%o + o) % o,
				(c[I+B] - c[I]*g[B]%d + d) % d}] = 1
			I++
		}
		for u <= A-B {
			i = u + B
			if h[H{(m[i] - m[u]*k[i-u]%o + o) % o,
				(x[i] - x[u]*g[i-u]%d + d) % d}] > 0 {
				q++
			}
			u++
		}
	}

	Print(q)
}