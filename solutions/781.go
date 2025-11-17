package main
import . "fmt"
func main() {
	n := 0
	b := 0
	a := 2

	Scan(&n)
	for 1 < n {
		a, b = a+b, a
		n--
	}

	Print(a + b)
}