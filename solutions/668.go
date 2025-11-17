package main
import . "fmt"
func main() {
	var n, m, s int

	Scan(&n, &m)
	for m > 0 {
		if n%2+m%4 < 1 || n%2 > 0 && m%4 == 2 {
			n++
			m -= 3
		}
		m++
		s++
	}
	m = -1
	if n%2 < 1 {
		m = s + n/2
	}

	Print(m)
}