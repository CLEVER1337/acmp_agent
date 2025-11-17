package main
import (
	. "fmt"
	. "math"
	. "sort"
)
func main() {
	var (
		r          [250]float64
		n, q, j, i int
	)

	Scan(&n)
	for j < n {
		Scan(&r[j])
		j++
	}

	Sort(Reverse(Float64Slice(r[:])))
	for i < n {
		j = i + 1
		for j < n {
			k := j + 1
			for k < n {
				x := 1 / r[i]
				y := 1 / r[j]
				z := 1 / r[k]
				x = x + y + z + 2*Sqrt(x*y+y*z+z*x)
				w := k + 1
				h := n
				for w < h {
					m := (w + h) / 2
					if r[m] <= 1/x {
						h = m
					} else {
						w = m + 1
					}
				}
				q += n - w
				k++
			}
			j++
		}
		i++
	}

	Print(q)
}