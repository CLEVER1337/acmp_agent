package main
import (
	. "fmt"
	. "math/big"
)
func main() {
	n := 0
	N := NewInt
	q := N(1)
	w := N(2)

	Scan(&n)
	for 2 < n {
		x := N(0)
		x.Add(q, w)
		q.Set(w)
		w.Set(x)
		n--
	}

	Print(q.Mul(w, w))
}