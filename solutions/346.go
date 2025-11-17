package main
import (
	. "fmt"
	. "sort"
)

func F(r []int) bool {
	a := 1 > 0
	j := len(r) - 1
	l := j
	i := j - 1
	for i >= 0 && r[i] >= r[i+1] {
		i--
	}
	if i >= 0 {
		for r[j] <= r[i] {
			j--
		}
		r[i], r[j] = r[j], r[i]
		i++
		for i < l {
			r[i], r[l] = r[l], r[i]
			i++
			l--
		}
		a = !a
	}
	return a
}

func main() {
	var (
		p, s, d    []int
		a, b, c, e int
		P          = Print
	)

	Scan(&a, &b, &c)
	for b > 0 {
		s = append(s, b%10)
		b /= 10
	}
	Ints(s)
	for {
		b = 0
		for _, v := range s {
			b = b*10 + v
		}
		if b != e {
			p = append(p, b)
			e = b
		}
		if F(s) {
			break
		}
	}

	for a > 0 {
		d = append(d, a%10)
		a /= 10
	}
	Ints(d)
	for {
		e = 0
		for _, v := range d {
			e = e*10 + v
		}
		a = c - e
		b = SearchInts(p, a)
		if b < len(p) && p[b] == a {
			P("YES ", e, a)
			return
		}
		if F(d) {
			break
		}
	}

	P("NO")
}