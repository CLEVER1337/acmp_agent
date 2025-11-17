package main
import (
	. "fmt"
	. "math/bits"
)
func main() {
	var k, p, i uint
	P := Println

	Scan(&i)
	for 0 < i {
		Scan(&k, &p)
		if k > 1<<p-1 {
			P("No solution")
		} else {
			P(TrailingZeros(k) + 1)
		}
		i--
	}
}