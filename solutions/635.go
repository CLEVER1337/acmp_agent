package main
import (
	. "fmt"
	. "sort"
)
type T struct {
	d, h int
}
func main() {
	var (
		w                []T
		v                []int
		a, n, m, e, l, i int
		t                T
		S = Scan
		P = Println
	)

	S(&n, &m)
	for l < n {
		S(&t.d, &t.h, &e)
		if t.h > 0 {
			w = append(w, t)
		}
		l++
	}

	for i < m {
		S(&a, &l, &e)
		if l > 0 {
			v = append(v, a)
		}
		i++
	}

	Slice(w, func(i, j int) bool {
		return w[i].h > w[j].h
	})

	if len(w) > 1 {
		a = len(w)/2 - 1
		i = 0
		for i < len(w) {
			if w[i].h > w[a].h || w[i].h == w[0].h {
				v = append(v, w[i].d)
			}
			i++
		}
	}

	Ints(v)

	P(len(v))
	for _, t := range v {
		P(t)
	}
}