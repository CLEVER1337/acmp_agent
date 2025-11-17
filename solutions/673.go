package main
import . "fmt"
type T uint
var (
	q, w, N T
	z       [10]T
)

func F(p T) {
	var m, e, d, o, k, i, c, x T
	e++
	d++
	k++
	if p == 9 {
		z[9] = N
		for i < 8 {
			i++
			z[9] -= z[i]
		}
		for d < 10 {
			i = 0
			o += d * z[d]
			for i < z[d] {
				k *= d
				m = m*10 + d
				i++
			}
			d++
		}
		if o != k {
			return
		}
		i = N
		d = 1
		for d < 10 {
			o = 0
			for o < z[d] {
				o++
				e = e * i / o
				i--
			}
			d++
		}
		q += e
		if w < 1 || m < w {
			w = m
		}
		return
	}
	i = 1
	for i < p {
		x += z[i]
		i++
	}
	for c <= N-x {
		z[p] = c
		F(p + 1)
		c++
	}
}

func main() {
	Scan(&N)

	F(1)
	if N < 2 {
		q++
		w--
	}

	Print(q, w)
}