package main
import (
	. "fmt"
	. "math/big"
)
func main() {
	var (
		n = 0
		k = 1
		X = "2"
		N = NewInt
		b = N(1)
		p = N(10)
	)

	Scan(&n)
	for k < n {
		k++
		var (
			u, v Int
			o    = b.Bit(0)
			d    = '2'
		)
		if o == 1 {
			d--
		}
		e := string(d) + X
		u.SetString(e, 10)
		X = e
		b.Div(&u, v.Lsh(N(1), uint(k)))
		p.Mul(p, N(10))
	}

	Print(X)
}