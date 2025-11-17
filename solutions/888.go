package main
import . "fmt"
func main() {
	var n, s, x int
	c := 3

	Scan(&n)
	for n > 0 {
		Scan(&x)
		s += c * x
		c += 4*x - 3
		if c < 3 {
			c = 3
		}
		n--
	}

	Print(s)
}