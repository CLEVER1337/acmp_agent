package main
import . "fmt"
func main() {
	n := 0
	g := 1
	h := 1

	Scan(&n)
	for 0 < n {
		g, h = (h+g)%10, g
		n--
	}

	Print(h)
}