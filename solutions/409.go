package main
import . "fmt"
func main() {
	var n, x, a, p, i float64

	Scan(&n, &a)
	n--
	for i < n {
		i++
		Scan(&p)
		x += (a + p) / 2
		a = p
	}

	Print(x / n)
}