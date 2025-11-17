package main
import . "fmt"
func main() {
	var n, i, m, j, c int
	s := "equal"

	Scan(&n, &m, &i, &j, &c)
	if m*n%2 > 0 {
		s = "white"
		if (i+j)%2 == c {
			s = "black"
		}
	}

	Print(s)
}