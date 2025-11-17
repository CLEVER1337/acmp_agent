package main
import (
	. "fmt"
	. "sort"
)
func main() {
	var (
		s    [1e4][2]int
		n, l int
		i    = 3
	)

	Scan(&n)
	for l < n {
		Scan(&s[l][0], &s[l][1])
		l++
	}

	Slice(s[:n], func(i, j int) bool {
		return s[i][0] < s[j][0]
	})

	e := s[1][1]
	l = e

	if n > 2 {
		l += s[2][1]
	}

	for i < n {
		g := e
		if e > l {
			g = l
		}
		g += s[i][1]
		e = l
		l = g
		i++
	}

	Print(l)
}