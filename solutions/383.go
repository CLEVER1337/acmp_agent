package main
import . "fmt"
func main() {
	n := 0
	i := 0

	Scan(&n)
	for 0 < n {
		i++
		x := i
		s := 0
		c := 0
		for x > 0 {
			s += x % 10
			x /= 10
			c++
		}
		if s%c < 1 {
			n--
		}
	}

	Print(i)
}