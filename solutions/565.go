package main
import (
	b "bufio"
	. "fmt"
	. "os"
	. "sort"
)
type T struct{ a, b, c int }
func main() {
	var (
		s                   = b.NewReader(Stdin)
		q, w                [1e5]int
		n, r, t, i, j, I, J int
		P                   = Println
	)

	Scan(&n, &r)
	a := make([]T, n)
	for i < n {
		Fscan(s, &a[i].a, &a[i].b)
		a[i].c = i + 1
		i++
	}

	Slice(a, func(i, j int) bool {
		return a[i].b < a[j].b
	})

	for _, v := range a {
		i = v.a - v.b
		if i > 0 {
			if (v.a - t) > (v.b-t)*r {
				P("Impossible")
				return
			}
			q[I] = t
			I++
			w[J] = v.c
			J++
			t += (i + r - 2) / (r - 1)
		}
	}

	for j < I {
		P(q[j], w[j])
		j++
	}
}