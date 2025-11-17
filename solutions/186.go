package main
import (
	. "fmt"
	. "sort"
)
func main() {
	var n, o, i int

	Scan(&n)
	a := make([]int, n)
	for i < n {
		Scan(&a[i])
		i++
	}

	Ints(a)
	h := a[n-1] - a[0]
	for o < h {
		m := (o + h) / 2
		n = len(a)
		d := [1e3]int{1}
		i = 1
		for i < n {
			i++
			j := 0
			for j < i-1 {
				if d[j] > 0 && a[i-1]-a[j] <= m {
					d[i] = 1
					break
				}
				j++
			}
		}
		if d[n] > 0 {
			h = m
		} else {
			o = m + 1
		}
	}

	Print(o)
}