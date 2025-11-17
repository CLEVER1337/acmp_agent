package main
import (
	. "fmt"
	. "sort"
)
type P struct {
	a, b float64
	c    int
}
func main() {
	n := 0
	i := 0
	a := 0.
	b := a

	Scan(&n, &a)
	q := make([]P, n)
	for i < n {
		Scan(&a, &b)
		q[i] = P{a - 1, b, i + 1}
		i++
	}

	Slice(q, func(i, j int) bool {
		return q[i].a/q[i].b > q[j].a/q[j].b
	})

	for _, v := range q {
		Println(v.c)
	}
}