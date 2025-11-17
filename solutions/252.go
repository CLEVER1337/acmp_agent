package main
import (
	. "fmt"
	. "math/big"
	. "sort"
)

type P struct {
	u string
	a int
}

func F(p P) *Rat {
	N := NewRat
	r := N(int64(p.a), 1)

	switch p.u[0] {
	case 'm':
		r.Quo(r, N(1e3, 1))
	case 'k':
		r.Mul(r, N(1e3, 1))
	case 'M':
		r.Mul(r, N(1e6, 1))
	case 'G':
		r.Mul(r, N(1e9, 1))
	}

	switch p.u[len(p.u)-1] {
	case 'p':
		r.Mul(r, N(16380, 1))
	case 't':
		r.Mul(r, N(1e6, 1))
	}

	return r
}

func main() {
	n := 0
	i := 0
	Scan(&n)

	q := make([]P, n)
	for i < n {
		v := 0
		s := ""
		Scan(&v, &s)
		q[i] = P{s, v}
		i++
	}

	SliceStable(q, func(i, j int) bool {
		return F(q[i]).Cmp(F(q[j])) < 0
	})

	for _, p := range q {
		Println(p.a, p.u)
	}
}