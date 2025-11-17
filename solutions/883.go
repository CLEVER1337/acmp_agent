package main
import . "fmt"
func main() {
	n := 0
	x := 0.
	y := x

	Scan(&n)
	for n > 0 {
		for x < .5 && n > 0 {
			Println(x, y)
			n--
			x += .01
		}
		x = 0
		y += .01
	}
}