package main
import (
	. "fmt"
	. "math"
)
func main() {
	n := 0
	k := 0.
	a := 0

	Scan(&n)
	for 0 < n {
		Scan(&k)
		a = int(k * Phi)
		Println(a, a+int(k))
		n--
	}
}