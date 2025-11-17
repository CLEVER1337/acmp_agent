package main
import . "fmt"
func main() {
	var a, b, c int

	Scan(&a, &b)
	for c < b - a {
		c++
		c *= 4
	}

	Print(c/4+a)
}