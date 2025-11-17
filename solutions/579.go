package main
import . "fmt"
func main() {
	var (
		p, e                   [1e4]int
		n, a, s, g, i, x, y, j int
		P                      = Println
	)

	Scan(&n)
	for i < n {
		i++
		Scan(&a)
		if a > 0 {
			p[x] = i
			s += a
			x++
		}
		if a < 0 {
			e[y] = i
			g -= a
			y++
		}
	}

	if s >= g {
		e = p
		y = x
	}

	P(y)
	for j < y {
		P(e[j])
		j++
	}
}