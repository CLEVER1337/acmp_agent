package main
import (
	. "fmt"
	. "sort"
)
func main() {
	var n, w, i, l, r, m, j int

	Scan(&n)
	a := []int{0, 1e9}
	for 0 < n {
		Scan(&l, &r)
		a = append(a, l, r)
	n--
	}

	Ints(a)
	for j < len(a) {
		if w < 1 || a[w-1] != a[j] {
			a[w] = a[j]
			w += 2
		}
		w--
	j++
	}

	for i < w {
		j = a[i+1]-a[i]
		if m < j { m = j }
	i += 2
	}

	Print(m)
}