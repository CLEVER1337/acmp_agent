package main
import (
	b "bufio"
	. "fmt"
	. "os"
	. "sort"
	. "strings"
)
type M map[string]int
type T map[any]M
func main() {
	var (
		n = 0
		q = T{}
		w = T{}
		I = b.NewReader(Stdin)
		J = Join
		P = Print
		F = Printf
	)

	Scanln(&n)
	for 0 < n {
		h, _ := I.ReadString('\n')
		p := Fields(h)
		g := p[0][0]
		if g < 66 {
			d := p[2]
			z := J(p[4:], " ")
			_, e := q[z]
			if !e {
				q[z] = M{}
			}
			_, e = w[d]
			if !e {
				w[d] = M{}
			}
			if q[z][d] > 0 {
				P(`Already exists
`)
			} else {
				q[z][d] = 1
				w[d][z] = 1
				P(`OK
`)
			}
		}
		if g == 82 {
			d := p[2]
			z := J(p[4:], " ")
			_, e := q[z]
			if !e {
				q[z] = M{}
			}
			_, e = w[d]
			if !e {
				w[d] = M{}
			}
			if q[z][d] < 1 {
				P(`Not found
`)
			} else {
				delete(q[z], d)
				delete(w[d], z)
				P(`OK
`)
			}
		}
		if g > 82 {
			var u []string
			c := 0
			z, e := w[J(p[1:], " ")]
			if e {
				for v := range z {
					u = append(u, v)
				}
				Strings(u)
				c = len(u)
			}
			F(`Results: %d site(s) found
`, c)
			if c > 10 {
				u = u[:10]
			}
			for i, v := range u {
				F(`%d) %s
`, i+1, v)
			}
		}
		n--
		if 0 < n {
			P(`=====
`)
		}
	}
}