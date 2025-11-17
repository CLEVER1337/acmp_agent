package main
import . "fmt"
func main() {
	var (
		a, s    [182]int
		g       [400][81]int
		n, i, k int
		S       = Scan
	)

	S(&n)
	for i < n {
		S(&a[i])
		i++
	}
	S(&k)

	for n >= 0 {
		s[n] = s[n+1] + a[n]
		m := 0
		for m < 80 {
			m++
			i = 0
			j := 0
			for j < m {
				j++
				q := s[n] - g[n+j][j]
				if q > i {
					i = q
				}
			}
			g[n][m] = i
		}
		n--
	}

	Print(g[0][k])
}