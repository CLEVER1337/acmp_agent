package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
type T struct{ i, j int }
func main() {
	var (
		a, d    [205][205]int
		q       []T
		g       = []int{0}
		n, l, i int
		r       = b.NewReader(Stdin)
		P       = Print
	)

	Scan(&n)
	for i < n {
		j := 0
		for j < n {
			w := 0
			Fscan(r, &w)
			if w > 0 {
				g = append(g, w)
				w = len(g) - 1
				q = append(q, T{i, j})
			} else {
				d[i][j]--
			}
			a[i][j] = w
			j++
		}
		i++
	}

	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		i = 0
		for i < 4 {
			k := u.i - 1 + i - i/3*2
			z := u.j + i - i/2*2 - i/3*2
			if k >= 0 && z >= 0 {
				w := d[u.i][u.j] + 1
				m := a[u.i][u.j]
				A := &a[k][z]
				D := &d[k][z]
				if *D < 0 {
					*D = w
					*A = m
					q = append(q, T{k, z})
				}
				if *D == w && *A != m {
					*A = 0
				}
			}
			i++
		}
	}

	for l < n {
		i = 0
		for i < n {
			P(g[a[l][i]], " ")
			i++
		}
		P(`
`)
		l++
	}
}