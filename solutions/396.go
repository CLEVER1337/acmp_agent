package main
import (
	b "bufio"
	. "fmt"
	. "os"
	. "sort"
)
type I int32
type P struct{ x, y, z I }
func main() {
	var (
		q                            [3e5]P
		w                            [1e5]I
		a, c, n, m, u, i, j, l, k, z I
		r                            = b.NewReader(Stdin)
		S                            = Fscan
	)

	Scan(&n, &m)
	for i < n {
		S(r, &a, &c)
		if a > c {
			c, a = a, c
		}
		q[k] = P{a, 1, -1}
		k++
		q[k] = P{c, -1, -1}
		k++
		i++
	}

	for j < m {
		S(r, &a)
		q[k] = P{a, 0, j}
		k++
		j++
	}

	Slice(q[:2*n+m], func(i, j int) bool {
		if q[i].x != q[j].x {
			return q[i].x < q[j].x
		}
		return q[i].y > q[j].y
	})

	for z < k {
		g := q[z]
		if g.y != 0 {
			u += g.y
		} else {
			w[g.z] = u
		}
		z++
	}

	for l < m {
		Println(w[l])
		l++
	}
}