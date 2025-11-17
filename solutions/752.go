package main
import . "fmt"
func main() {
	var (
		a, b, c, d, s [6e3]int
		l, r          int
		i             = 2
	)

	Scan(&l, &r)
	s[1] = 1
	c[0] = 1
	for i <= l {
		a, b, c, d = b, c, d, a
		for j := range d {
			d[j] = 0
		}
		j := 0
		for j < i/2 {
			j++
			d[j] = (a[j-1] + b[j-1]) % r
			s[i] = (s[i] + d[j]*s[j]) % r
		}
		i++
	}

	Print(s[l])
}