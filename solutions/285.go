package main
import . "fmt"
func main() {
	var n, m, i, a, b, p int
	s := "yes"

	Scan(&n, &m)
	for i < n {
		Scan(&p)
		a += p
		if b < p {
			b = p
		}
		i++
	}
	if b > m || a-n+1 < m {
		s = "no"
	}

	Print(s)
}