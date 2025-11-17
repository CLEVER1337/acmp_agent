package main
import . "fmt"
func main() {
	var (
		x, y [20]int
		n, m, k, a, l, i int
	)

	Scan(&n, &m, &k)
	for l < k {
		Scan(&x[l], &y[l])
	l++
	}
	for i < n {
		j := 0
		for j < m {
			h := n + m
			l = 0
			for l < k {
				v := i-x[l]+1
				if v < 0 { v = -v }
				w := j-y[l]+1
				if w < 0 { w = -w }
				if h > v + w {
					h = v + w
				}
			l++
			}
			if h > a {
				a = h
			}
		j++
		}
	i++
	}

	Print(a)
}