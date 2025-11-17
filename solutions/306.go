package main
import . "fmt"
func main() {
	n := 0
	z := 0
	c := 'B'
	Scan(&n)

	q := make([]int, n)
	s := make([]rune, n)

	for z < n {
		q[z] = z
		z++
	}

	for len(q) > 0 {
		s[q[0]] = c
		q = q[1:]
		c = 148 - c
		if len(q) > 0 {
			q = append(q, q[0])
			q = q[1:]
		}
	}

	Print(string(s))
}