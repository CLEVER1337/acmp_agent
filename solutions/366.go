package main
import . "fmt"
func main() {
	var (
		n, s, a, j, i int
		m, q          [30]int
		P             = Print
	)

	Scan(&n, &s)
	for j < n {
		Scan(&m[j])
		a += m[j]
		j++
	}

	n--
	for i < 1<<n {
		j = 0
		for q[j] > 0 {
			q[j] = 0
			j++
			a += 2 * m[j]
		}
		q[j] = 1
		a -= 2 * m[j+1]
		if a == s {
			j = 0
			for j < n {
				v := "+"
				if q[j] > 0 {
					v = "-"
				}
				P(m[j], v)
				j++
			}
			P(m[n], "=", s)
			return
		}
		i++
	}

	P("No solution")
}