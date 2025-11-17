package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
type T [2e3]int
func main() {
	var (
		a          [1e3]T
		c          T
		n, m, q, i int
		r          = b.NewReader(Stdin)
		s          = ""
	)

	Scan(&n, &m)
	for i < n {
		Fscan(r, &s)
		j := 0
		for j < m {
			if s[j] > 48 {
				a[i][j] = 1
			}
			j++
		}
		i++
	}

	for m > 0 {
		var d []int
		i = 0
		for i < n {
			c[i]++
			c[i] *= a[i][m-1]
			i++
		}
		i = 0
		for i <= n {
			k := len(d)
			for k > 0 && c[i] < c[d[k-1]] {
				k--
				h := c[d[k]]
				d = d[:k]
				w := i
				if k > 0 {
					w = i - d[k-1] - 1
				}
				if h*w > q {
					q = h * w
				}
			}
			d = append(d, i)
			i++
		}
		m--
	}

	Print(q)
}