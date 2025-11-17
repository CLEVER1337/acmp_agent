package main
import . "fmt"
func main() {
	var (
		s       [101][101]int
		n, i, z int
	)

	Scan(&n)
	for i < n {
		Scan(&s[i][i])
		i++
	}
	n--
	for z < n {
		i = 0
		for i <= n-z {
			i++
			v := &s[i+z][i-1]
			a := s[i+z-1][i-1]
			b := s[i+z][i]
			if a < b {
				a, b = b, a
			}
			*v = b
			if (n-z)&1 > 0 {
				*v = a
			}
		}
		z++
	}

	Print(s[n][0])
}