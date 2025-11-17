package main
import (
	. "fmt"
	. "sort"
)

type A struct {
	a int
	b []string
}

type M map[string]int

func main() {
	var (
		q []A
		o = M{}
		u = map[string]M{}
		n = 0
		s = ""
		P = Print
	)

	Scan(&n)
	for 0 < n {
		Scan(&s)
		x := []byte(s)
		Slice(x, func(i, j int) bool {
			return x[i] < x[j]
		})
		y := string(x)
		o[y]++
		if u[y] == nil {
			u[y] = M{}
		}
		u[y][s] = 1
		n--
	}

	for l, v := range u {
		var t []string
		for w := range v {
			t = append(t, w)
		}
		Strings(t)
		q = append(q, A{o[l], t})
	}

	Slice(q, func(i, j int) bool {
		a := q[i]
		b := q[j]
		if a.a != b.a {
			return a.a > b.a
		}
		return a.b[0] < b.b[0]
	})

	for i, v := range q {
		if i < 5 {
			P("Group of size ", v.a, ": ")
			for _, w := range v.b {
				P(w, " ")
			}
			P(`.
`)
		}
	}
}