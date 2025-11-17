package main
import (
	. "fmt"
	. "math/big"
)

var (
	x, y *Int
	b    = 1
	s    = ""
)

func F(q **Int) {
	Scan(&s)
	i := 0
	for i < len(s) {
		h := s[i:] + s[:i]
		if h[0] > 48 {
			var u Int
			u.SetString(h, 10)
			if *q == nil || u.Cmp(*q)*b > 0 {
				*q = &u
			}
		}
		i++
	}
	b = -b
}

func main() {
	F(&x)
	F(&y)
	Print(y.Sub(x, y))
}