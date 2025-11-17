package main
import (
	. "fmt"
	. "math/big"
)
type I [151]Int
func main() {
	var (
		b, e I
		s    = ""
		r    = NewInt(1)
	)

	Scan(&s)
	k := len(s) / 2
	b[0] = *r
	for _, v := range s {
		var (
			q    I
			l, j int
		)
		if v < 41 {
			for l < k {
				l++
				q[l].Set(&b[l-1])
			}
			r.Add(r, &q[0])
			b = q
			for j <= k {
				e[j].Add(&e[j], &b[j])
				j++
			}
		} else {
			for l < k {
				e[l].Set(&e[l+1])
				l++
			}
			r.Add(r, &e[0])
			for j <= k {
				b[j].Add(&b[j], &e[j])
				j++
			}
		}
	}

	Print(r)
}