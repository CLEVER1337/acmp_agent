package main
import (
	. "fmt"
	. "sort"
)
type T struct{ a, b int }
func main() {
	var (
		y             []int
		h             [1e4]int
		n, d, i, l, x int
		P             = Println
	)

	Scan(&n, &d)
	q := make([]T, n)
	for i < n {
		Scan(&x)
		q[i] = T{x, i}
		i++
	}

	Slice(q, func(i, j int) bool {
		return q[i].a < q[j].a
	})

	for _, v := range q {
		for i, s := range y {
			if v.a-s > d {
				h[v.b] = i
				y[i] = v.a
				goto A
			}
		}
		h[v.b] = len(y)
		y = append(y, v.a)
	A:
	}

	P(len(y))
	for l < n {
		P(h[l] + 1)
		l++
	}
}