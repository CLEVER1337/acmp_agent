package main
import (
	b "bufio"
	. "fmt"
	. "os"
	. "sort"
)
func main() {
	var (
		p       [1e5][]int
		a, n, i int
		s       = b.NewReader(Stdin)
	)

	Scan(&n)
	for i < n {
		Fscan(s, &a)
		p[i] = []int{a, i + 1}
		i++
	}

	Slice(p[:n], func(i, j int) bool {
		return p[i][0] < p[j][0]
	})

	m := p[1][0] - p[0][0]
	u := p[0][1]
	b := p[1][1]

	i = 2
	for i < n {
		a = p[i][0] - p[i-1][0]
		if m > a {
			m = a
			u = p[i-1][1]
			b = p[i][1]
		}
		i++
	}

	Print(m, u, b)
}