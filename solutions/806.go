package main
import (
	b "bufio"
	. "fmt"
	. "os"
	. "sort"
)
func main() {
	var (
		a, c          [1e5]int
		n, u, q, l, i int
		w             = 1 << 60
		r             = b.NewReader(Stdin)
		S             = Fscan
		P             = Println
	)

	S(r, &n)
	x := make([]int, n)
	for i < n {
		x[i] = i
		S(r, &a[i])
		q += a[i]
		i++
	}
	for l < n {
		S(r, &c[l])
		l++
	}

	Slice(x, func(i, j int) bool {
		return a[x[i]]+c[x[i]] > a[x[j]]+c[x[j]]
	})

	for _, v := range x {
		u += a[v]
		if u+c[v] < w {
			w = u + c[v]
		}
	}

	if w > q {
		for _, v := range x {
			P(v + 1)
		}
		return
	}

	P(-1)
}