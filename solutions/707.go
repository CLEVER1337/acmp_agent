package main

import (
	. "fmt"
	. "strconv"
)

type S = string
type T []M
type M struct {
	a int
	b T
	c S
}

func F(s T) S {
	var b S
	for _, p := range s {
		b += p.c + Itoa(p.a) + " "
	}
	return b
}

func main() {
	var (
		h       []S
		u       T
		g       = 1
		s       = ""
		b, z, i int
		P       = Println
	)

	Scan(&s)
	for i < len(s) {
		if i == len(s)-1 || s[i] != s[i+1] {
			u = append(u, M{g, nil, S(s[i])})
			g = 0
		}
		i++
		g++
	}

	q := [][]T{{u}, {}, {}}
	m := map[S]M{}
	for m[""].a < 1 {
		if b == len(q[z]) {
			b = 0
			z++
			z %= 3
			if len(q[z]) < 1 {
				z++
				z %= 3
			}
		}
		u := q[z][b]
		b++
		j := 0
		for i, p := range u {
			l := make(T, len(u[:i]))
			r := make(T, len(u[i+1:]))
			copy(l, u[:i])
			copy(r, u[i+1:])
			y := len(l) - 1
			k := 0
			for y >= 0 && k < len(r) && l[y].c == r[k].c {
				if l[y].a+r[k].a > 2 {
					y--
				} else {
					l[y].a += r[k].a
				}
				k++
			}
			v := append(append(T{}, l[:y+1]...), r[k:]...)
			w := F(v)
			_, O := m[w]
			if !O {
				a := p.c + Itoa(j)
				y = 1
				if p.a < 2 {
					a += " " + a
					y = 2
				}
				m[w] = M{m[F(u)].a + y, u, a}
				q[(z+y)%3] = append(q[(z+y)%3], v)
			}
			j += p.a
		}
	}

	r := m[""]
	P(r.a)
	for r.a > 0 {
		h = append(h, r.c)
		r = m[F(r.b)]
	}
	i = len(h)
	for i > 0 {
		i--
		P(h[i])
	}
}
