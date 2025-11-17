package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
func main() {
	var (
		g       [2e4][]int
		h       []int
		s       = []int{1}
		n, u, v int
		r       = b.NewReader(Stdin)
		P       = Println
	)

	Scan(&n, &n)
	for 0 < n {
		Fscan(r, &u, &v)
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
		n--
	}

	for len(s) > 0 {
		j := len(s) - 1
		u = s[j]
		v = len(g[u]) - 1
		if v >= 0 {
			s = append(s, g[u][v])
			g[u] = g[u][:v]
		} else {
			h = append(h, u)
			n++
			s = s[:j]
		}
	}

	P(n - 1)
	for _, v := range h {
		P(v)
	}
}