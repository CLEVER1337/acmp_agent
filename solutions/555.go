package main
import . "fmt"
const R = 3001
type T uint32
var (
	q, h       [R]int
	d          [R][]int
	o          [R][R]T
	a          T = 1
	n, p, l, z int
)

func F(i int) T {
	for _, v := range d[i] {
		F(v)
	}
	p = h[i] + 1
	for p < R {
		o[i][p] = 0
		p++
	}
	var s T
	x := R
	for x > 0 {
		x--
		s += o[i][x]
		p = q[i]
		if p < 0 {
			o[-p][x] *= s
		}
		if p == x {
			return s
		}
	}
	return 0
}

func main() {
	Scan(&n)
	for l < n {
		l++
		Scan(&p, &h[l])
		q[l] = p
		if p < 0 {
			d[-p] = append(d[-p], l)
		}
		for j := range o[l] {
			o[l][j] = 1
		}
	}

	for z < n {
		z++
		if q[z] >= 0 {
			a *= F(z)
		}
	}

	Print(a)
}