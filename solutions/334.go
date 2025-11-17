package main
import (
	. "fmt"
	. "sort"
)
func main() {
	var (
		e                   []int
		u, n, j, l, h, m, w int
		o                   = 3600
		s                   = `
%d:%02d:%02d`
	)

	Scan(&n)
	for l < n {
		Scanf(s, &h, &m, &w)
		w += h*o + m*60
		e = append(e, w)
		u += w
		l++
	}

	Ints(e)
	w = -1
	for i, t := range e {
		l = n*t - u + (n-i-1)*43200
		if w < 0 || l < w {
			w = l
			j = t
		}
	}

	Printf(s, j/o, (j%o)/60, j%60)
}