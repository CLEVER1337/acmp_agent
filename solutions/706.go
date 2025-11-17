package main
import . "fmt"
func main() {
	r := .0
	x := r
	y := r

	Scan(&r, &x, &y)
	if x < 0 {
		x = -x
	}

	Print(r * x / (2*r - y))

}