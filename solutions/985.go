package main
import (
	. "fmt"
	. "math/big"
)
func main() {
	var (
		n, q int64
		z    = map[any]*Int{}
		p    = ""
		t    = p
		S    = Scan
		N    = NewInt
		a    = N(0)
		h    = N(20)
		g    = N(4)
	)

	S(&n)
	for 0 < n {
		S(&p, &q)
		z[p] = N(q)
		n--
	}

	S(&n)
	for 0 < n {
		S(&p, &t)
		var (
			d    [50]Int
			s    = ""
			x    = N(0)
			u    = N(1)
			i, j int
		)
		for _, c := range t {
			if c == 91 {
				s = ""
			} else if c == 93 {
				q = 0
				for _, v := range s {
					q = q*10 + int64(v-48)
				}
				d[j] = *N(q)
				j++
			} else {
				s += string(c)
			}
		}

		for i < j {
			v := g
			if i == j-1 {
				v = z[p]
			}
			x.Add(x, a.Mul(u, a.Add(h, a.Mul(&d[i], v))))
			u.Mul(u, &d[i])
			i++
		}

		x.Add(x, g)
		Println(x)
		n--
	}
}