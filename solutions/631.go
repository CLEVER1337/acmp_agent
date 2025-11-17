package main
import . "fmt"
func main() {
	n := 0
	a := 1
	b := 1
	c := 1

	Scan(&n)
	if n < 2 {
		c = 0
	}

	for b < n {
		a, b, c = b, a+b, c+1
	}
	Print(c)
}