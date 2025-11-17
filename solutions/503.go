package main
import . "fmt"
type T int16
var (
	q, z, m, u, o [22]T
	a             [1 << 22][3]T
	n, i, w       int
	x, y, g, h    T
	e             = ' '
	k             = 1
	P             = Print
)

func F() T {
	W := a[w]
	return W[h]&1023 +
		o[i]*(W[1]>>10) +
		u[i]*(W[2]>>10) +
		W[0]
}

func main() {

	Scan(&n)
	for i < n {
		Scanf("\n%c %d %d %d %d", &e, &z[i], &m[i], &u[i], &o[i])
		q[i] = 2
		if e > 79 {
			q[i]--
		}
		i++
	}

	for k < 1<<n {
		g = 9000
		i = 0
		for i < n {
			if 1<<i&k > 0 {
				w = k - 1<<i
				h = q[i]
				if F() < g {
					g = F()
					x = a[w][1] + z[i] + (h-1)<<10
					y = a[w][2] + m[i] + (2-h)<<10
				}
			}
			i++
		}
		a[k][0] = g
		a[k][1] = x
		a[k][2] = y
		k++
	}

	k = 1<<n - 1
	P(a[k][0], 0)
	for k > 0 {
		i = 0
		for i < n {
			if 1<<i&k > 0 {
				w = k - 1<<i
				h = q[i]
				if F() == a[k][0] {
					P(" ", i+1)
					k = w
					break
				}
			}
			i++
		}
	}

	P(" 0")
}