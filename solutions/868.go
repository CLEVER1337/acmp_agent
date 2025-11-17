package main
import (
	b "bufio"
	. "fmt"
	. "os"
	. "sort"
)
type T [400]int
func main() {
	var (
		a, c                [400]T
		t                   T
		n, m, w, i, l, j, z int
		s                   = b.NewReader(Stdin)
	)

	Scan(&n, &m)
	for i < n {
		j = 0
		for j < m {
			Fscan(s, &a[i][j])
			j++
		}
		i++
	}

	q := a[0][0]
	for l < n {
		j = 0
		for j < m {
			t[j] = j
			v := a[l][j]
			if v > q {
				q = v
				w = l
			}
			j++
		}
		l++
	}

	a[0], a[w] = a[w], a[0]

	Slice(t[:m], func(i, j int) bool {
		return a[0][t[i]] > a[0][t[j]]
	})

	for z < n {
		j = 0
		for j < m {
			c[z][j] = a[z][t[j]]
			j++
		}
		z++
	}

	Slice(c[1:], func(i, j int) bool {
		k := 0
		for k < m {
			o := c[i+1][k]
			v := c[j+1][k]
			if o != v {
				return o > v
			}
			k++
		}
		return 1 < 0
	})

	Print(c[n-1][m-1])
}