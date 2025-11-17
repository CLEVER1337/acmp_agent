package main
import (
	. "fmt"
	. "math/big"
)
func main() {
	var (
		m, n Int
		z, s Rat
		N    = NewInt
		w    = N(1)
		k    = N(1)
	)

	Scan(&m, &n)
	for m.Cmp(w) > -1 {
		k.Div(&n, &m)
		if z.SetFrac(w, k).Cmp(s.SetFrac(&m, &n)) > 0 {
			k.Add(k, w)
		}
		Println(k)
		m.Sub(m.Mul(&m, k), &n)
		n.Mul(&n, k)
		k.GCD(k, k, &m, &n)
		m.Div(&m, k)
		n.Div(&n, k)
	}
}