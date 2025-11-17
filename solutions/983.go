package main
import (
	b "bufio"
	. "fmt"
	. "os"
	. "sort"
)
type M struct { t, w, d, s int }
func main() {
	var i, k, n, l int
	r := b.NewReader(Stdin)

	Scan(&n)
	a := make([]M, n)
	for i < n {
		Fscan(r, &a[i].t, &a[i].w)
		a[i].d = i
		i++
	}

	Slice(a, func(i, j int) bool {
		return a[i].w < a[j].w
	})

	a[0].s = a[0].t * a[0].w

	for l < n-1 {
		l++
		c := a[l].t * a[l].w
		a[l].s = a[l-1].s
		if a[l].s < c {
			a[l].s = c
		}
	}

	Slice(a, func(i, j int) bool {
		return a[i].d < a[j].d
	})

	for k < n {
		Println(a[k].s)
		k++
	}
}