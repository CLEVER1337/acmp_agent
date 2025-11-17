package main
import . "fmt"
func main() {
	var x, y, s int

	Scan(&x, &y)
	if x != 0 && y%x < 1 && y/x > 0 {
		n := y / x
		d := 2

		for d*d <= n {
			if n%d < 1 {
				n /= d
				s += d
				d--
			}
			d++
		}
		s += n + 1
	}

	if x == y {
		s = 1
	}

	Print(s - 1)
}