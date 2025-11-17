package main
import . "fmt"
func main() {
	x := 0
	c := 1
	d := 2

	Scan(&x)
	for d < 1e3 {
		e := 0
		for x%d < 1 {
			x /= d
			e++
		}
		if e > 0 {
			c *= e
		}
		d++
	}

	Print(c)
}