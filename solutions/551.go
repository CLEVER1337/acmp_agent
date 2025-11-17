package main
import (
	. "fmt"
	. "math"
)
func main() {
	var a, c, h, b float64
	s := "YES"

	Scan(&a, &c, &h, &b)
	if h-Sqrt(a*a-c*c)+c > b {
		s = "NO"
	}

	Print(s)
}