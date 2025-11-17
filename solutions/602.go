package main
import . "fmt"
func main() {
	var n, x, y, a, b, m int
	m = 7e4

	Scan(&n, &a)
	for 1 < n {
		Scan(&b)
		if m > b-a {
			m = b - a
			x = a
			y = b
		}
		a = b
		n--
	}

	Print(x, y)
}